from datetime import datetime
import math as maths
import random
from typing import Any, Callable, List

def timeit(func: Callable):
    def wrapper(*args):
        start_time = datetime.now()
        func(*args)
        print(f"Function {func.__name__} ran in {datetime.now()-start_time}")
    
    return wrapper
    

@timeit
def search(_list: List[Any], target: Any) -> Any:
    start_list = _list
    current_list = start_list.copy()

    iterations = 0
    while True:
        iterations += 1
        split_index = maths.ceil(len(current_list)/2)
        found_index = pow(split_index, iterations)
        current_item = current_list[split_index]
        
        if target == current_list[split_index]:
            print(f"Found {target} at position {found_index}")
            break

        if target > current_item:
            current_list = current_list[split_index:]
        elif target < current_item:
            current_list = current_list[:split_index]

search(list(range(0, 100)), 84)
