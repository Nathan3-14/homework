from random import choice, randint
from typing import Dict, List, Tuple

def combine_dicts(dict_1: dict, dict_2: dict) -> dict:
    def add_if_exists(in_dict: dict, target_dict: dict) -> None:
        for key, value in in_dict.items():
            if key in target_dict.keys():
                target_dict[key] += value
                continue
            target_dict[key] = value

    to_return = {}
    d1, d2 = dict_1.copy(), dict_2.copy()

    add_if_exists(d1, to_return)
    add_if_exists(d2, to_return)
    
    return to_return
    
storage_type = Dict[
    str, Tuple[                 # name: data
        Tuple[int, int], int    # minimum value, weigth
    ]
]

class LootTable:
    def __init__(self, storage: storage_type) -> None:
        self.storage = storage
        # ? Format:
        # {
        #    "name": (("min", "max"), "weight")
        #*   "gold": ((1, 3), 1)
        # }
    
    def get_item(self, count: int=1) -> dict:
        choices = []
        for item, item_data in self.storage.items():
            for i in range(item_data[1]):
                choices.append({
                    item: randint(item_data[0][0], item_data[0][1])
                }) #* Adds item name and amount
        to_return = {}
        for i in range(count):
            to_return = combine_dicts(to_return, choice(choices))
        return to_return

class Inventory:
    def __init__(self) -> None:
        self.storage = {}
    
    def add_item(self, item: str, amount: int) -> None:
        if item in self.storage.keys():
            self.storage[item] += amount #* Adds item count if key exists
        else:
            self.storage[item] = amount #* Creates the item key if it doesn't exist
        # print(f"  DEBUG: {self.storage}") #! DEBUG
    
    def gain_loot(self, loot_table: LootTable, roll_count: int) -> None:
        self.storage = combine_dicts(self.storage, loot_table.get_item(roll_count))
        # print(f"  DEBUG: {self.storage}") #! DEBUG
    
    def use_item(self, item: str, amount: int) -> bool:
        if item in self.storage.keys():
            if self.storage[item] >= amount: #* Checks if there are enough items in storage to use the items
                self.storage[item] -= amount #* Subtracts the amount of the item from the total
                if self.storage[item] == 0:
                    self.storage.pop(item) #* Removes the item if the amount is zero
                return True
            else:
                return False
        else:
            return False
    
    def __str__(self) -> str:
        #* Dislays the inventory nicely
        converted = f""
        for item, amount in self.storage.items():
            converted += f"{amount} {item}, "
        converted = converted[:-2]
        return converted


if __name__ == "__main__":
    t_inv = Inventory()
    t_table = LootTable({
        "gold": ((1, 3), 2),
        "key": ((1, 1), 1)
    })

    t_inv.add_item("gold", 2)
    t_inv.gain_loot(t_table, 1)

    