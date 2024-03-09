from typing import Any, Dict, Tuple, List
from icecream import ic

def get_input(message: str, data_type: Any, num_range: Tuple[int, int]=(0,0)):
    output = None
    while True:
        try:
            output = data_type(input(message))
            if data_type == int and not (num_range[0] <= output <= num_range[1]):
                continue
        except ValueError:
            continue
        break
    
    return output

def get_factors(number: int, factors: Dict[int, List[int]], max_recursion: int=5):
    max_recursion -= 1
    get_factors(0, {}, max_recursion)

range_list: List[int] = list(range(1, 11))
factors = {
    key: [
        i for i in range_list
        if key % i == 0
    ]
    for key in range_list
}
print(factors)
_input: int = get_input("Enter a number between 1 and 10\n>> ", int, (1, 10))


