import sys
import time
import keyboard

def display_map() -> None:
    for line in map:
        output = ""
        for char in line:
            if char.isdigit():
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
    current_position = map.index(player_index)
    target_position = current_position - len(map[0])
    player_index = target_position


map = [
    "#####",
    "#012#",
    "#345#",
    "#####"
]
player_index = 0

display_map()
keyboard.add_hotkey("w", move_up)
keyboard.wait("w")
display_map()