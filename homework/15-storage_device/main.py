from rich.console import Console
from rich.prompt import Prompt

console = Console()

types = {
    "solid state": {
        "durability": 3,
        "reliability": 3,
        "cost": 1
    },
    "magnetic": {
        "durability": 2,
        "reliability": 2,
        "cost": 2
    },
    "optical": {
        "durability": 1,
        "reliability": 1,
        "cost": 3
    }
}

needs = {
    "durability": Prompt.ask("Do you need durability", choices=["y", "n"]),
    "reliability": Prompt.ask("Do you need reliability", choices=["y", "n"]),
    "cost": Prompt.ask("Do you need cost", choices=["y", "n"])
}

best = "default"
totals = {"default": 0}
for name, values in types.items():
    totals[name] = 0
    for property, value in values.items():
        totals[name] += value if needs[property] == "y" else 0
    if totals[name] > totals[best]:
        best = name
print(best)
