from random import choice
import time
from typing import Any, Generic, TypeVar, List, Type, Callable


erase_line = "\033[F\033[K"

def erase(count: int=1) -> None:
    for _ in range(count):
        print(erase_line, end="")

def true() -> bool:
    return True
CustomType = TypeVar('CustomType')
def fancy_input(
        message: str,
        _type: Type[CustomType],
        options: List[Any]=[],
        caps_sensitive: bool=False
    ) -> CustomType:

    def no_option_condition(_option) -> bool: 
        try:
            _type(_option) # type: ignore #! Complains about too many inputs
        except TypeError:
            return False
        return True
    def options_condition(_option) -> bool:
        try:
            _tmp = _type(_option) # type: ignore #! Complains about too many inputs
        except TypeError:
            return False
        return _tmp in options

    _input = ""
    condition = true
    if options == []:
        condition = no_option_condition
    else:
        condition = options_condition
    
    first = True
    while not condition(_input):
        if not first:
            print("Enter valid value")
        _input = input(message)
        if not caps_sensitive:
            _input = _input.lower()
        first = False

    return _type(_input) # type: ignore #! Complains about too many inputs


if __name__ == "__main__":
    ROLL_WEIGHTS = {
        "1": 5,
        "2": 5,
        "3": 3,
        "4": 2,
        "5": 1
    }
    ROLLS = []
    for num, weight in ROLL_WEIGHTS.items():
        for _ in range(weight):
            ROLLS.append(num)

    COST = 1
    money = 10

    while money > 0:
        if fancy_input(f"You have £{money}. Spend {COST} to spin? (y/n)", str, ["y", "n"]) == "n":
            break
        money -= COST
        

        print("\n\n")
        for _ in range(20):
            roll_1 = choice(ROLLS)
            roll_2 = choice(ROLLS)
            roll_3 = choice(ROLLS)

            erase(3)

            print("/-------\\")
            print(f"| {roll_1} {roll_2} {roll_3} |")
            print("|_______|")
            time.sleep(0.1)

        if roll_1 == roll_2 and roll_2 == roll_3: #type:ignore
            win_amount = roll_1 * 2 #type:ignore
            print(f"WINNER! Won £{win_amount}!")
            money += win_amount
    
    print(f"You ended at £{money}, you lost £{10-money}!")
