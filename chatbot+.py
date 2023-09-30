user = input("What is your name?\n>> ")

keywords = {
    ["hello", "hi"]:    f"Hello there {user}",
    ["goodbye", "bye"]: f"Goodbye {user}",
}

while True:
    response = input(">> ")

    for option in list(keywords.keys()):
        if response in option: pass