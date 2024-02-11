# -*- coding: utf-8 -*-

import sys
import time
import keyboard
import random
import os
from auth import Auth

class Game:
    def __init__(self, maps):
        self.player_start_positon = [2, 2]  # ?  x, y (0 indexed)
        self.player_positon = self.player_start_positon
        self.current_map = maps["1"]
        self.running = True
        self.end_message = ""
        self.action = False
        self.inventory = []
        self.bonus_message = ""



    def write_error(self, function, error: Exception) -> None:
        if not os.path.exists("errors.log"):
            a = open("errors.log", "w")
            a.close()

        with open("errors.log", "a") as f:
            f.write(f"{function}: {error}\n")


    def display_map(self, clear: bool = True) -> None:
        if clear:
            self.clear_lines(len(self.current_map["map"]) + 2)
        else:
            print("\n"*3)
        try:
            self.main_output = ""
            for y_index, line in enumerate(
                self.current_map["map"]
            ):  # * Goes through each horizontal line in the map
                self.output = ""
                for x_index, char in enumerate(
                    line
                ):  # * Goes through each character in the line
                    if (
                        x_index == self.player_positon[0] and y_index == self.player_positon[1]
                    ):  # * Checks for the players position being the current position
                        self.output += "@"
                    else:
                        self.output += char
                self.main_output += self.output + "\n"
            self.main_output = (
                self.main_output.strip()
            )  # * Removes the extra \n at the end of the output
        except Exception as e:
            self.write_error(self.display_map, e)
        finally:
            if do_fancy_tiles:
                for key, tile in fancy_tiles.items():
                    self.main_output = self.main_output.replace(key, tile)
            self.inventory_output = f"Inventory: {self.inventory}"
            print(self.bonus_message)
            print(self.inventory_output)
            print(self.main_output)
            self.bonus_message = ""

    def replace_char_at_index(self, text: str, replace: str, index: int) -> str:
        self.to_return = list(text)
        self.to_return[index] = replace
        return("".join(self.to_return))

    def clear_lines(self, count: int = 1) -> None:
        for _ in range(count):
            sys.stdout.write("\033[F")
            sys.stdout.write("\033[K")


    def move_player(self, x: int, y: int) -> None:
        # print(f"Player moving {x},{y}") #! DEBUG

        self.player_vector = [x, y]
        self.old_player_positon = self.player_positon.copy()

        # * Adds the player_vector to the current player position
        self.player_positon[0] += self.player_vector[0]
        self.player_positon[1] += self.player_vector[1]

        # * Checks if the players next position is a wall
        try:
            self.current_tile = self.current_map["map"][self.player_positon[1]][self.player_positon[0]]

            if self.current_tile == "#":  # ? Wall tile
                # * Resets the players position
                self.player_positon = self.old_player_positon
            
            if self.current_tile == "~":  # ? End tile
                self.end_message = "You won!"
                self.finish()
            
            if self.current_tile == "+": # ? Key tile
                self.bonus_message = "You got a key!"
                self.inventory.append("key")
                self.current_map["map"][self.player_positon[1]] = self.replace_char_at_index(self.current_map["map"][self.player_positon[1]], " ", self.player_positon[0]) #* Replaces the key's location with a blank character

            
            if self.current_tile == "=": # ? Lock tile
                if "key" in self.inventory:
                    self.inventory.remove("key")
                    self.current_map["map"][self.player_positon[1]] = self.replace_char_at_index(self.current_map["map"][self.player_positon[1]], " ", self.player_positon[0]) #* Replaces the lock's location with a blank character
                else:
                    self.bonus_message = "You need a key"
                    self.player_positon = self.old_player_positon
            
            if self.current_tile == "*": # ? Chest tile
                self.loot = [("gold", (2, 3)), ("key", (1))]

                self.loot_type = random.choice(self.loot)
                self.inventory.append(
                    self.loot_type[0]
                )

                self.current_map["map"][self.player_positon[1]] = self.replace_char_at_index(self.current_map["map"][self.player_positon[1]], " ", self.player_positon[0]) #* Replaces the chests's location with a blank character
                    


            self.door_check()
            self.action = True
        except Exception as e:  # * Checks if the player is off the map
            self.write_error(self.move_player, f"{e.__context__} : {e}")
            self.player_positon = self.old_player_positon

    def door_check(self):
        for door_position, door_data in self.current_map["doors"].items(): #* Iterates through all doors in the current room
            if tuple(self.player_positon) == door_position:
                self.player_positon = door_data[2].copy() #? New player position
                self.current_map = maps[door_data[1]].copy()


    def finish(self):
        self.running = False


auth = Auth(json_path="./login.json")
user = auth.check_user(input("Enter your username\n>> "), input("Enter your password\n>> "))
if not user:
    quit()


bonus_message = ""
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
    "*": default_tile,  # ? Chest
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
    "##∧##",  # ? 0,0 -> 4,0
    "#* ##",
    "## +#",
    "#####"   # ? 0,3 -> 4,3
]


maps = {
    "1": {
        "map": map_1,
        "doors": {
            (9, 1): ["right", "2", [1, 1]], #? door_pos: [door_direction, new_map, new_player_pos]
        }
    },
    "2": {
        "map": map_2,
        "doors": {
            (0, 1): ["left", "1", [8, 1]],
            (2, 3): ["down", "3", [2, 1]]
        },
        "from": {
            "left": [1, 1],
            "down": [2, 2]
            },
    },
    "3": {
        "map": map_3,
        "doors": {
            (2, 0): ["up", "2", [2, 2]]
        }
    }
}




option = input("Fancy tiles? y/n\n>> ")
if option.lower() == "y":
    do_fancy_tiles = True
option = input("Erase each time? y/n\n>> ")
do_clear = option.lower() == "y"

game = Game(maps)
print("\n" * len(game.current_map["map"]))

keyboard.add_hotkey("w", game.move_player, (0, -1))
keyboard.add_hotkey("s", game.move_player, (0, 1))
keyboard.add_hotkey("a", game.move_player, (-1, 0))
keyboard.add_hotkey("d", game.move_player, (1, 0))
keyboard.add_hotkey("esc", game.finish)

while game.running:
    game.display_map(do_clear)
    while not game.action:
        pass
    game.action = False
print(game.end_message)
input("Here's all of your moves!\n  (Press enter to continue and exit)\n")
