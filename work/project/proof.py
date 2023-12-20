import sys
import time
import keyboard

def is_position(char: chr, pos_list: list) -> bool:
    return char in pos_list

def display_map() -> None:
    for line in map:
        output = ""
        for char in line:
            if is_position(char, ["a"]):
                if int(char) == player_index:
                    output += "@"
                else:
                    output += " "
            else:
                output += char
        print(output)

def clear_lines(count: int = 1) -> None:
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")



def move_up():
    pass
    #!
    # global player_index
    # current_position = 0
    # target_position = current_position - len(map[0])
    # player_index = target_position
    #!


map = [
    "##########",
    "abc##jklmn",
    "#defghi###",
    "##########"
]
player_index = 3

display_map()
keyboard.add_hotkey("w", move_up)
keyboard.wait("w")
display_map()