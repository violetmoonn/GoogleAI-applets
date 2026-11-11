"""Built-in tools. Enable the ones you want per agent in agents/*.yaml."""

import ast
import datetime
import math
import operator
import os
import subprocess
from pathlib import Path

from toolkit import tool

MEMORY_FILE = Path(os.environ.get("AGENT_MEMORY_FILE", "memory.md"))


@tool(description="Get the current local date and time.")
def get_time() -> str:
    return datetime.datetime.now().strftime("%A %Y-%m-%d %H:%M:%S")


_OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
        ast.Div: operator.truediv, ast.Pow: operator.pow, ast.Mod: operator.mod,
        ast.FloorDiv: operator.floordiv, ast.USub: operator.neg, ast.UAdd: operator.pos}
_FUNCS = {k: getattr(math, k) for k in ("sqrt", "sin", "cos", "tan", "log", "log10", "exp", "floor", "ceil")}
_FUNCS.update(abs=abs, round=round, pi=math.pi, e=math.e)


def _eval(node):
    if isinstance(node, ast.Expression):
        return _eval(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_eval(node.left), _eval(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_eval(node.operand))
    if isinstance(node, ast.Name) and node.id in _FUNCS:
        return _FUNCS[node.id]
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in _FUNCS:
        return _FUNCS[node.func.id](*[_eval(a) for a in node.args])
    raise ValueError("unsupported expression")


@tool(description="Evaluate a math expression exactly, e.g. 'sqrt(2) * (3 + 4) ** 2'.",
      params={"expression": "The arithmetic expression to evaluate."})
def calculator(expression: str) -> str:
    return str(_eval(ast.parse(expression, mode="eval")))


@tool(description="List the files and folders in a directory.",
      params={"path": "Directory path (default: current folder)."})
def list_dir(path: str = ".") -> str:
    entries = sorted(Path(path).iterdir())
    return "\n".join(f"{e.name}/" if e.is_dir() else e.name for e in entries) or "(empty)"


@tool(description="Read a UTF-8 text file and return its contents.",
      params={"path": "Path to the file."})
def read_file(path: str) -> str:
    text = Path(path).read_text(encoding="utf-8")
    return text if len(text) < 100_000 else text[:100_000] + "\n...[truncated at 100k chars]"


@tool(description="Create or overwrite a text file with the given contents.", confirm=True,
      params={"path": "Path to the file.", "contents": "Full file contents."})
def write_file(path: str, contents: str) -> str:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(contents, encoding="utf-8")
    return f"Wrote {len(contents)} chars to {p}"


@tool(description="Run a shell command and return its output (60s timeout).", confirm=True,
      params={"command": "The shell command to run."})
def run_shell(command: str) -> str:
    r = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=60)
    out = (r.stdout + r.stderr).strip()
    return f"exit code {r.returncode}\n{out[:20_000]}"


@tool(description="Save a fact to long-term memory so it is remembered in future sessions.",
      params={"note": "A short, self-contained fact worth remembering."})
def remember(note: str) -> str:
    MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
    with MEMORY_FILE.open("a", encoding="utf-8") as f:
        f.write(f"- {note.strip()}\n")
    return "Saved to memory."
