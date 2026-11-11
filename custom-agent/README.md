# Customizable Claude agent

A terminal chat agent powered by Claude. Each agent's personality, model,
reasoning effort and tools are set in a YAML file, and you can add your own
tools by dropping a Python file in `plugins/`.

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...
```

## Run

```bash
python agent.py                      # agents/default.yaml
python agent.py --agent coder        # agents/coder.yaml
python agent.py --agent researcher -p "What changed in the latest Python release?"
python agent.py --list               # show agents and tools
```

In chat: `/tools`, `/config`, `/reset`, `/save chat.json`, `/load chat.json`, `/exit`.

## Make your own agent

Copy `agents/default.yaml` to `agents/myagent.yaml` and edit:

| Key | What it does |
|---|---|
| `name` | Name shown in the chat |
| `model` | `claude-opus-5-5` (default), `claude-sonnet-5-5`, `claude-haiku-5-5`, `claude-fable-5-2` |
| `effort` | `low` / `medium` / `high` / `xhigh` / `max` — how hard Claude thinks (and how many tokens it spends) |
| `system_prompt` | The agent's instructions and personality |
| `tools` | Local tools from `plugins/` (`python agent.py --list` shows them) |
| `server_tools` | `web_search`, `web_fetch` — run by Anthropic, no setup needed |
| `auto_approve` | `true` lets tools like `write_file` / `run_shell` run without asking |
| `memory_file` | File the `remember` tool writes to; it's loaded into the prompt next session |
| `show_thinking` | Print a summary of Claude's reasoning as it works |
| `fallbacks` | `default` re-runs a declined request on another model; `null` turns it off (Haiku has no server-side fallback, so set `null` there) |
| `max_tokens`, `max_tool_rounds` | Output and loop limits |

## Add a tool

Create `plugins/my_tools.py`:

```python
from toolkit import tool

@tool(description="Look up a customer's order status.",
      params={"order_id": "The order number."})
def order_status(order_id: str) -> str:
    return my_database.lookup(order_id)
```

Then add `order_status` to an agent's `tools:` list. Type hints become the
tool's input schema; pass `confirm=True` to make the agent ask before running it.

## Built-in tools

`get_time`, `calculator`, `list_dir`, `read_file`, `write_file` (asks first),
`run_shell` (asks first), `remember`, `roll_dice` (example plugin).
