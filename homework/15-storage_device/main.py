from rich.console import Console
from rich.prompt import Prompt

console = Console()

types = {
    "magnetic": {
        "capacity": 3,
        "access_speed": 2,
        "portability": 3,
        "durability": 1,
        "reliability": 3,
        "cost": 2
    },
    "solid state": {
        "capacity": 2,
        "access_speed": 3,
        "portability": 3,
        "durability": 3,
        "reliability": 3,
        "cost": 1
    },
    "optical": {
        "capacity": 1,
        "access_speed": 1,
        "portability": 3,
        "durability": 2,
        "reliability": 3,
        "cost": 3
    }
}

needs = {
    "capacity": Prompt.ask("Do you need capacity", choices=["y", "n"]),
    "access_speed": Prompt.ask("Do you need access speed", choices=["y", "n"]),
    "portability": Prompt.ask("Do you need portability", choices=["y", "n"]),
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
