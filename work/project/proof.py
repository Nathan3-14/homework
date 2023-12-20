import sys
import time
import keyboard


def is_position(char: chr, pos_list: list) -> bool:
    return char in pos_list


def display_map() -> None:
    clear_lines(len(map))
    try:
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
    except:
        pass
    finally:
        print(main_output)


def clear_lines(count: int = 1) -> None:
    for _ in range(count):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")


def move_player(x: int, y: int) -> list:
    global player_positon

    player_vector = [x, y]
    old_player_positon = player_positon.copy()

    #* Adds the player_vector to the current player position
    player_positon[0] += player_vector[0]
    player_positon[1] += player_vector[1]

    #* Checks if the players next position is a wall
    #TODO Add try excpet for this
    if map[player_positon[1]][player_positon[0]] == "#":
        #* Resets the players position
        player_positon = old_player_positon



def finish():
    global running
    running = False


map = [
    "##########",  # ?  0,0 -> 9,0
    "#  ##    #",  # ?  0,1 -> 9,1
    "##     ###",  # ?  0,2 -> 9,2
    "##########",  # ?  0,3 -> 9,3
]
player_start_positon = [2, 2]
player_positon = player_start_positon
# ?  x, y (0 indexed)
running = True

keyboard.add_hotkey("w", move_player, (0, -1))
keyboard.add_hotkey("s", move_player, (0, 1))
keyboard.add_hotkey("a", move_player, (-1, 0))
keyboard.add_hotkey("d", move_player, (1, 0))
keyboard.add_hotkey("esc", finish)


print("\n" * len(map))
while running:
    display_map()
    pass
