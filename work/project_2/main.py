import json
from os import error
import random



def display_list(in_list: list):
    to_return = ""
    for item in in_list:
        to_return += f"{item} "
    return to_return

def error_quit():
        print("Incorrect username or password")
        quit()

def main():
    users = {
        "nathan": "password"
    }
    
    user_in = input("Enter username ")
    pass_in = input("Enter password ")

    if user_in not in users.keys():
        error_quit()
    if users[user_in] == pass_in:
        error_quit()

    with open("songs.json", "r") as f:
        data = json.load(f)
        data.pop("Artist")

        data_list = list(data.items())
        random.shuffle(data_list)
        data = dict(data_list)


    points = 0


    for artist, song in data.items():
        song_display = [word[0] for word in song.split(' ')]
        print(f"{artist} - {display_list(song_display)}")

        chances = 2
        while chances > 0:
            guess = input("Guess the song! ").lower()
            if guess == song.lower():
                print("You got it!")
                if chances == 2:
                    points += 3
                else:
                    points += 1
                break
            else:
                print("Try again!")
                chances -= 1
        if chances == 0:
            print("l bozo, you lost")
            break
    print(f"You got {points} points!")

if __name__ == "__main__":
    main()