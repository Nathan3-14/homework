import json
import random

def display_list(in_list: list):
    to_return = ""
    for item in in_list:
        to_return += f"{item} "
    return to_return

def main():
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