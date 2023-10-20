with open('./alphabet.txt', 'r') as f:
    alphabet = []
    for character in f.read():
        alphabet.append(character)