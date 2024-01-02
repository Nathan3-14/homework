# -*- coding: utf-8 -*-

import sys
import time
import keyboard
import os


def write_error(error: Exception) -> None:
    if not os.path.exists("errors.log"):
        a = open("errors.log", "w")
        a.close()

    with open("errors.log", "a") as f:
        f.write(f"{error}\n")


def display_map(clear: bool = True) -> None:
    global map
    global current_map
    global fancy_tiles

    if clear:
        clear_lines(len(current_map["map"]))
    else:
        print("\n"*2)
    try:
        main_output = ""
        for y_index, line in enumerate(
            current_map["map"]
        ):  # * Goes through each horizontal line in the map
            output = ""
            for x_index, char in enumerate(
                line
            ):  # * Goes through each character in the line
                if (
                    x_index == player_positon[0] and y_index == player_positon[1]
                ):  # * Checks for the players position being the current position
                    output += "@"
                else:
                    output += char
            main_output += output + "\n"
        main_output = (
            main_output.strip()
        )  # * Removes the extra \n at the end of the output
    except:
        pass
    finally:
        if do_fancy_tiles:
            for key, tile in fancy_tiles.items():
                main_output = main_output.replace(key, tile)
        print(main_output)


def clear_lines(count: int = 1) -> None:
    for _ in range(count):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")


def move_player(x: int, y: int) -> list:
    global player_positon
    global current_map
    global map
    global end_message
    global action

    player_vector = [x, y]
    old_player_positon = player_positon.copy()

    # * Adds the player_vector to the current player position
    player_positon[0] += player_vector[0]
    player_positon[1] += player_vector[1]

    # * Checks if the players next position is a wall
    try:
        current_tile = current_map["map"][player_positon[1]][player_positon[0]]

        if current_tile == "#":  # ? Wall tile
            # * Resets the players position
            player_positon = old_player_positon

        if current_tile == ">":  # ? Right door tile
            try:
                current_map = maps[current_map["right"]]  # * Moves map right
                player_positon = current_map["from"][
                    "left"
                ].copy()  # * Gets starting position
            except Exception as e:
                write_error(e)
        if current_tile == "<":  # ? Left door tile
            try:
                current_map = maps[current_map["left"]]  # * Moves map left
                player_positon = current_map["from"][
                    "right"
                ].copy()  # * Gets starting position
            except Exception as e:
                write_error(e)
        
        if current_tile == "v":  # ? Down door tile
            try:
                current_map = maps[current_map["down"]]  # * Moves map left
                player_positon = current_map["from"][
                    "up"
                ].copy()  # * Gets starting position
            except Exception as e:
                write_error(e)
        
        if current_tile == "^":  # ? Left door tile
            try:
                current_map = maps[current_map["up"]]  # * Moves map left
                player_positon = current_map["from"][
                    "down"
                ].copy()  # * Gets starting position
            except Exception as e:
                write_error(e)
        
        
        if current_tile == "~":  # ? End tile
            end_message = "You won!"
            finish()
        action = True
    except Exception as e:  # * Checks if the player is off the map
        write_error(e)
        player_positon = old_player_positon


def finish():
    global running
    running = False


# ⛶ 🞃🞂🞁🞀

default_tile = "\u25CD"
fancy_tiles = {
    "#": "\u25FC",  # ? Wall
    "@": "\u26F6",  # ? Player
    "~": "\u25FB",  # ? End tile
    "v": "\u23F7",  # ? Down arrow
    "^": "\u23F6",  # ? Up arrow
    ">": "\u23F5",  # ? Right arrow
    "<": "\u23F4",  # ? Left arrow
    "+": default_tile,  # ? Key
    "=": default_tile,  # ? Lock
}
do_fancy_tiles = False


map_1 = [
    "##########",  # ?  0,0 -> 9,0
    "#  ##    >",
    "##     ###",
    "##########",  # ?  0,3 -> 9,3
]
map_2 = [
    "#######",  # ?  0,0 -> 7,0
    "<   #~#",
    "##   =#",
    "##v####",  # ?  0,3 -> 7,3
]
map_3 = [
    "##^##",  # ? 0,0 -> 4,0
    "#  ##",
    "## +#",
    "#####"   # ? 0,3 -> 4,3
]
maps = {
    "1": {
        "map": map_1,
        "from": {
            "right": [8, 1]
            },
        "right": "2"
    },
    "2": {
        "map": map_2,
        "from": {
            "left": [1, 1],
            "down": [2, 2]
            },
        "left": "1",
        "down": "3"
    },
    "3": {
        "map": map_3,
        "from": {
            "up": [2, 1]
            },
        "up": "2"
    }
}
new_maps = {
    "1": {
        "map": map_1,
        "doors": {
            [9, 1]: ["right", "2", [1, 1]], #? door_pos: [door_direction, new_map, new_player_pos]
        }
    },
    "2": {
        "map": map_2,
        "doors": {
            [0, 1]: ["left", "1", [8, 1]],
            [2, 3]: ["down", "3", [2, 1]]
        },
        "from": {
            "left": [1, 1], #!
            "down": [2, 2]
            },
    },
    "3": {
        "map": map_3,
        "doors": {
            [2, 1]: ["up", "2", [2, 2]]
        }
    }
}


current_map = maps["1"]
player_start_positon = [2, 2]  # ?  x, y (0 indexed)
player_positon = player_start_positon

running = True
action = False
end_message = ""

keyboard.add_hotkey("w", move_player, (0, -1))
keyboard.add_hotkey("s", move_player, (0, 1))
keyboard.add_hotkey("a", move_player, (-1, 0))
keyboard.add_hotkey("d", move_player, (1, 0))
keyboard.add_hotkey("esc", finish)


option = input("Fancy tiles? y/n\n>> ")
if option.lower() == "y":
    do_fancy_tiles = True
option = input("Erase each time? y/n\n>> ")
do_clear = option.lower() == "y"

print("\n" * len(current_map["map"]))

while running:
    display_map(do_clear)
    while not action:
        pass
    action = False
print(end_message)
input("Here's all of your moves!\n  (Press enter to continue and exit)\n")
