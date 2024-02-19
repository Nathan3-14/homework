class Inventory:
    def __init__(self) -> None:
        self.storage = {}
    
    def add_item(self, item: str, amount: int) -> None:
        if item in self.storage.keys():
            self.storage[item] += amount
        else:
            self.storage[item] = amount
        print(f"  DEBUG: {self.storage}")
    
    def use_item(self, item: str, amount: int) -> bool:
        if item in self.storage.keys():
            if self.storage[item] >= amount:
                self.storage[item] -= amount
                return True
            else:
                return False
        else:
            return False
    
    def __str__(self) -> str:
        converted = f""
        for item, amount in self.storage.items():
            converted += f"{amount} {item}, "
        converted = converted[:-2]
        return converted

class LootTable:
    def __init__(self, storage: dict) -> None:
        self.storage = storage
    
    def get_item(self) -> dict:
        return {}

if __name__ == "__main__":
    t_inv = Inventory()
    t_inv.add_item("gold", 3)
    t_inv.add_item("gold", 6)
    t_inv.add_item("potion", 1)

    if t_inv.use_item("gold", 6):
        print("Can spend!")
    else:
        print("Can't spend!")
    
    print(t_inv)
    
    