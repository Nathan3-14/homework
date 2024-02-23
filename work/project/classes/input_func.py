from typing import Union


def get_input_with_type(message: str, type: Union[int, str, bool, float]) -> type:
    user_input = input(message)
    while True:
        try:
            user_input = type(user_input) #! IGNORE ERROR
            break
        except ValueError:
            user_input = input(message)
    return user_input

if __name__ == "__main__":
    number_input = get_input_with_type("Enter a number!\n>> ", int) #! IGNORE ERROR
    number_input = get_input_with_type("Enter a string!\n>> ", str) #! IGNORE ERROR
    number_input = get_input_with_type("Enter a boolean!\n>> ", bool) #! IGNORE ERROR
    number_input = get_input_with_type("Enter a float!\n>> ", float) #! IGNORE ERROR