"""Tool registry: turn plain Python functions into Claude tools.

Usage (in any file under plugins/):

    from toolkit import tool

    @tool(description="Roll an N-sided die.")
    def roll_die(sides: int = 6) -> str:
        ...

The JSON schema is built from the function's type hints; parameters
without defaults are required. Mark risky tools with `confirm=True`
so the agent asks before running them.
"""

import importlib.util
import inspect
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

_PY_TO_JSON = {str: "string", int: "integer", float: "number", bool: "boolean", list: "array", dict: "object"}


@dataclass
class Tool:
    name: str
    description: str
    func: Callable[..., Any]
    schema: Dict[str, Any]
    confirm: bool = False

    def definition(self, eager: bool) -> Dict[str, Any]:
        d = {"name": self.name, "description": self.description, "input_schema": self.schema}
        if eager:
            d["eager_input_streaming"] = True
        return d


REGISTRY: Dict[str, Tool] = {}


def tool(description: str, name: Optional[str] = None, confirm: bool = False,
         params: Optional[Dict[str, str]] = None):
    """Register a function as a tool. `params` maps argument name -> description."""
    params = params or {}

    def wrap(func):
        props, required = {}, []
        for pname, p in inspect.signature(func).parameters.items():
            jtype = _PY_TO_JSON.get(p.annotation, "string")
            prop = {"type": jtype}
            if pname in params:
                prop["description"] = params[pname]
            props[pname] = prop
            if p.default is inspect.Parameter.empty:
                required.append(pname)
        schema = {"type": "object", "properties": props, "required": required,
                  "additionalProperties": False}
        t = Tool(name or func.__name__, description, func, schema, confirm)
        REGISTRY[t.name] = t
        return func

    return wrap


def validate(args: Any, schema: Dict[str, Any]) -> Optional[str]:
    """Return an error string if args don't match the (flat) schema, else None."""
    if not isinstance(args, dict):
        return "input must be a JSON object"
    for r in schema.get("required", []):
        if r not in args:
            return f"missing required field '{r}'"
    checks = {"string": str, "integer": int, "number": (int, float), "boolean": bool,
              "array": list, "object": dict}
    for k, v in args.items():
        spec = schema["properties"].get(k)
        if spec is None:
            return f"unexpected field '{k}'"
        want = checks.get(spec.get("type"))
        if want and (not isinstance(v, want) or (spec["type"] in ("integer", "number") and isinstance(v, bool))):
            return f"field '{k}' should be {spec['type']}"
    return None


def load_plugins(folder: Path) -> List[str]:
    """Import every .py file in `folder` so its @tool functions register."""
    loaded = []
    if not folder.is_dir():
        return loaded
    for path in sorted(folder.glob("*.py")):
        if path.name.startswith("_"):
            continue
        spec = importlib.util.spec_from_file_location(f"plugins.{path.stem}", path)
        mod = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = mod
        spec.loader.exec_module(mod)
        loaded.append(path.stem)
    return loaded
