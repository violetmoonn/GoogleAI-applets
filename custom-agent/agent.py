#!/usr/bin/env python3
"""A customizable Claude agent for the terminal.

    python agent.py                  # uses agents/default.yaml
    python agent.py --agent coder    # uses agents/coder.yaml
    python agent.py --agent coder -p "one-shot question"   # answer once and exit
"""

import argparse
import json
import os
import sys
from pathlib import Path

import anthropic
import yaml

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

from toolkit import REGISTRY, load_plugins, validate  # noqa: E402

SERVER_TOOLS = {
    "web_search": {"type": "web_search_20260209", "name": "web_search"},
    "web_fetch": {"type": "web_fetch_20260209", "name": "web_fetch"},
}

DEFAULTS = {
    "name": "Assistant",
    "model": "claude-opus-5-5",
    "effort": "high",            # low | medium | high | xhigh | max
    "max_tokens": 64000,
    "show_thinking": False,      # print a summary of Claude's reasoning
    "fallbacks": "default",      # server-side refusal fallback; set to null to disable
    "system_prompt": "You are a helpful assistant.",
    "tools": [],                 # names of local tools from plugins/
    "server_tools": [],          # web_search, web_fetch
    "auto_approve": False,       # if true, tools marked confirm=True run without asking
    "memory_file": None,         # path; contents are added to the system prompt
    "max_tool_rounds": 25,
}

DIM, BOLD, CYAN, YELLOW, RED, RESET = "\033[2m", "\033[1m", "\033[36m", "\033[33m", "\033[31m", "\033[0m"


def load_config(name_or_path: str) -> dict:
    path = Path(name_or_path)
    if not path.suffix:
        path = ROOT / "agents" / f"{name_or_path}.yaml"
    with path.open() as f:
        cfg = {**DEFAULTS, **(yaml.safe_load(f) or {})}
    unknown = [t for t in cfg["server_tools"] if t not in SERVER_TOOLS]
    if unknown:
        sys.exit(f"Unknown server tools {unknown}. Options: {list(SERVER_TOOLS)}")
    return cfg


class Agent:
    def __init__(self, cfg: dict):
        self.cfg = cfg
        self.client = anthropic.Anthropic()
        self.messages = []
        missing = [t for t in cfg["tools"] if t not in REGISTRY]
        if missing:
            sys.exit(f"Unknown tools {missing}. Available: {sorted(REGISTRY)}")
        self.tools = [REGISTRY[t] for t in cfg["tools"]]

    # ---------- request building ----------
    def system_prompt(self) -> str:
        prompt = self.cfg["system_prompt"].strip()
        mem = self.cfg.get("memory_file")
        if mem and Path(mem).exists() and Path(mem).read_text().strip():
            prompt += "\n\n<memory>\nThings you saved in earlier sessions:\n" + Path(mem).read_text() + "</memory>"
        return prompt

    def request_params(self) -> dict:
        thinking = {"type": "adaptive"}
        if self.cfg["show_thinking"]:
            thinking["display"] = "summarized"
        params = dict(
            model=self.cfg["model"],
            max_tokens=self.cfg["max_tokens"],
            system=self.system_prompt(),
            messages=self.messages,
            thinking=thinking,
            output_config={"effort": self.cfg["effort"]},
            cache_control={"type": "ephemeral"},
        )
        tools = [t.definition(eager=True) for t in self.tools]
        tools += [SERVER_TOOLS[name] for name in self.cfg["server_tools"]]
        if tools:
            params["tools"] = tools
        if self.cfg.get("fallbacks"):
            params["betas"] = ["server-side-fallback-2026-07-01"]
            params["fallbacks"] = self.cfg["fallbacks"]
        return params

    # ---------- one model call, streamed to the terminal ----------
    def call_model(self):
        printed_text = False
        with self.client.beta.messages.stream(**self.request_params()) as stream:
            for event in stream:
                if event.type == "content_block_start":
                    block = event.content_block
                    if block.type in ("tool_use", "server_tool_use"):
                        print(f"\n{CYAN}⚙ {block.name}{RESET}", end="", flush=True)
                    elif block.type == "text" and printed_text:
                        print()
                elif event.type == "content_block_delta":
                    if event.delta.type == "text_delta":
                        print(event.delta.text, end="", flush=True)
                        printed_text = True
                    elif event.delta.type == "thinking_delta" and self.cfg["show_thinking"]:
                        print(f"{DIM}{event.delta.thinking}{RESET}", end="", flush=True)
            msg = stream.get_final_message()
        print()
        return msg

    # ---------- run local tools ----------
    def run_tool(self, block) -> dict:
        result = {"type": "tool_result", "tool_use_id": block.id}
        tool = REGISTRY.get(block.name)
        if tool is None or tool not in self.tools:
            return {**result, "content": f"Error: unknown tool {block.name}", "is_error": True}
        err = validate(block.input, tool.schema)
        if err:
            return {**result, "content": f"Error: invalid input ({err}). Please retry.", "is_error": True}
        print(f"{DIM}   {json.dumps(block.input)[:300]}{RESET}")
        if tool.confirm and not self.cfg["auto_approve"]:
            ans = input(f"{YELLOW}   Allow {tool.name}? [y/N] {RESET}").strip().lower()
            if ans not in ("y", "yes"):
                return {**result, "content": "The user declined to run this tool.", "is_error": True}
        try:
            out = tool.func(**block.input)
            return {**result, "content": str(out)}
        except Exception as e:  # report tool failures back to Claude
            return {**result, "content": f"Error: {type(e).__name__}: {e}", "is_error": True}

    # ---------- the agent loop for one user turn ----------
    def send(self, user_text: str) -> None:
        checkpoint = len(self.messages)
        self.messages.append({"role": "user", "content": user_text})
        for _ in range(self.cfg["max_tool_rounds"]):
            try:
                msg = self.call_model()
            except ValueError as e:  # tool input JSON the SDK couldn't parse at all
                print(f"{RED}Malformed tool input from the model ({e}); retrying.{RESET}")
                continue

            if msg.stop_reason == "refusal":
                print(f"{RED}The model declined this request.{RESET}")
                del self.messages[checkpoint:]
                return
            if msg.stop_reason == "max_tokens":
                print(f"{RED}Hit max_tokens ({self.cfg['max_tokens']}); raise it in the config.{RESET}")
                if any(b.type == "tool_use" for b in msg.content):
                    del self.messages[checkpoint:]   # never run a truncated tool call
                else:
                    self.messages.append({"role": "assistant", "content": msg.content})
                return

            self.messages.append({"role": "assistant", "content": msg.content})
            if msg.stop_reason == "pause_turn":       # server tool hit its iteration limit
                continue
            if msg.stop_reason != "tool_use":
                return

            results = [self.run_tool(b) for b in msg.content if b.type == "tool_use"]
            self.messages.append({"role": "user", "content": results})
        print(f"{RED}Stopped after {self.cfg['max_tool_rounds']} tool rounds.{RESET}")

    # ---------- save / load ----------
    def dump_messages(self):
        def conv(c):
            if isinstance(c, list):
                return [b.model_dump(mode="json", exclude_none=True, by_alias=True) if hasattr(b, "model_dump") else b for b in c]
            return c
        return [{"role": m["role"], "content": conv(m["content"])} for m in self.messages]


HELP = """Commands:
  /reset         start a new conversation
  /save FILE     save the conversation as JSON
  /load FILE     load a saved conversation
  /tools         list this agent's tools
  /config        show the active config
  /exit          quit"""


def repl(agent: Agent) -> None:
    cfg = agent.cfg
    print(f"{BOLD}{cfg['name']}{RESET} {DIM}({cfg['model']}, effort {cfg['effort']}) — /help for commands{RESET}")
    while True:
        try:
            line = input(f"\n{BOLD}you ›{RESET} ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if not line:
            continue
        if line.startswith("/"):
            cmd, _, arg = line.partition(" ")
            if cmd in ("/exit", "/quit"):
                return
            elif cmd == "/help":
                print(HELP)
            elif cmd == "/reset":
                agent.messages = []
                print("Conversation cleared.")
            elif cmd == "/save" and arg:
                Path(arg).write_text(json.dumps(agent.dump_messages(), indent=2))
                print(f"Saved to {arg}")
            elif cmd == "/load" and arg:
                agent.messages = json.loads(Path(arg).read_text())
                print(f"Loaded {len(agent.messages)} messages.")
            elif cmd == "/tools":
                for t in agent.tools:
                    print(f"  {t.name}{' (asks first)' if t.confirm else ''} — {t.description}")
                for s in cfg["server_tools"]:
                    print(f"  {s} (server-side)")
                if not agent.tools and not cfg["server_tools"]:
                    print("  (none)")
            elif cmd == "/config":
                print(yaml.safe_dump(cfg, sort_keys=False))
            else:
                print(HELP)
            continue
        print(f"{BOLD}{cfg['name']} ›{RESET} ", end="")
        safe_send(agent, line)


def safe_send(agent: Agent, line: str) -> None:
        try:
            agent.send(line)
        except KeyboardInterrupt:
            print(f"\n{YELLOW}Interrupted.{RESET}")
        except anthropic.AuthenticationError:
            print(f"{RED}Authentication failed: set ANTHROPIC_API_KEY.{RESET}")
        except anthropic.RateLimitError:
            print(f"{RED}Rate limited; wait a moment and try again.{RESET}")
        except anthropic.BadRequestError as e:
            print(f"{RED}Bad request: {e.message}{RESET}")
        except anthropic.APIStatusError as e:
            print(f"{RED}API error {e.status_code}: {e.message}{RESET}")
        except anthropic.APIConnectionError:
            print(f"{RED}Could not reach the API; check your connection.{RESET}")


def main():
    ap = argparse.ArgumentParser(description="Customizable Claude agent")
    ap.add_argument("--agent", "-a", default="default", help="agent name in agents/ or a path to a .yaml file")
    ap.add_argument("--prompt", "-p", help="send one message and exit")
    ap.add_argument("--list", action="store_true", help="list agents and tools, then exit")
    args = ap.parse_args()

    pre = load_config(args.agent)
    if pre.get("memory_file"):
        mem = Path(pre["memory_file"])
        if not mem.is_absolute():
            mem = ROOT / mem
        pre["memory_file"] = str(mem)
        os.environ["AGENT_MEMORY_FILE"] = str(mem)
    load_plugins(ROOT / "plugins")

    if args.list:
        print("Agents:", ", ".join(p.stem for p in sorted((ROOT / "agents").glob("*.yaml"))))
        print("Tools: ", ", ".join(sorted(REGISTRY)), "+ server:", ", ".join(SERVER_TOOLS))
        return

    agent = Agent(pre)
    if args.prompt:
        safe_send(agent, args.prompt)
    else:
        repl(agent)


if __name__ == "__main__":
    main()
