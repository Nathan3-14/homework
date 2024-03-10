from typing import Any, Tuple


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


factors = {
    1: [1],
    2: [2],
    3: [3],
    4: [2, 2],
    5: [5],
    6: [3, 2],
    7: [7],
    8: [2, 2, 2],
    9: [3, 3],
    10: [5, 2]
}

print(factors[get_input("Enter a number between 1 and 10\n>> ", int, (1, 10))])
