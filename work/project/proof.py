import sys
import time
import keyboard


def is_position(char: chr, pos_list: list) -> bool:
    return char in pos_list


def display_map() -> None:
    clear_lines(len(map))
    main_output = ""
    for y_index, line in enumerate(map):
        output = ""
        for x_index, char in enumerate(line):
            if x_index == player_positon[0] and y_index == player_positon[1]:
                output += "@"
            else:
                output += char
        main_output += output + "\n"
    main_output = main_output.strip()
    print(main_output)


def clear_lines(count: int = 1) -> None:
    for _ in range(count):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")


def sense_collision(player_positon: list) -> bool:
    pass


def move_up():
    player_positon[1] -= 1


def move_down():
    player_positon[1] += 1


def move_left():
    player_positon[0] -= 1


def move_right():
    player_positon[0] += 1


def finish():
    global running
    running = False


map = [
    "##########",  #?  0,0 -> 9,0
    "#  ##     ",  #?  0,1 -> 9,1
    "##     ###",  #?  0,2 -> 9,2
    "##########",  #?  0,3 -> 9,3
]
player_positon = [2, 2]
#?  x, y (0 indexed)
running = True

keyboard.add_hotkey("w", move_up)
keyboard.add_hotkey("s", move_down)
keyboard.add_hotkey("a", move_left)
keyboard.add_hotkey("d", move_right)
keyboard.add_hotkey("esc", finish)

print("\n" * len(map))
while running:
    display_map()
