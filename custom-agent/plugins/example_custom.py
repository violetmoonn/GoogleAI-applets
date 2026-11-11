"""Example of a custom tool. Copy this file to add your own.

Any .py file in plugins/ is loaded automatically. Add the tool's name to
an agent's `tools:` list in agents/*.yaml to give that agent access.
"""

import random

from toolkit import tool


@tool(description="Roll one or more dice and return the results.",
      params={"sides": "Number of sides per die.", "count": "How many dice to roll."})
def roll_dice(sides: int = 6, count: int = 1) -> str:
    rolls = [random.randint(1, sides) for _ in range(max(1, min(count, 100)))]
    return f"Rolled {rolls} (total {sum(rolls)})"
