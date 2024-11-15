from random import randint as random
from alphabet import alphabet


def encrypt(text: str, keyshift: int = None):
    output = ""
    if keyshift == None:
        keyshift = random(1, 26)
    for letter in text:
        letter_index = alphabet.index(letter) + keyshift

        if letter_index > 26:
            letter_index -= 26

        output += alphabet[letter_index]
    return output


if __name__ == "__main__":
    in_text = input("Enter text to encrypt\n>> ")
    in_shift = input("Enter the keyshift (or None for random)\n>> ")
    if in_shift.lower() == "none":
        in_shift = None
    else:
        in_shift = int(in_shift)
    encrypt_text = encrypt(in_text, in_shift)
    print(encrypt_text)
