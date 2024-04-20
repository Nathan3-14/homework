names = ["Berners-Lee", "Hopper", "Lovelace", "Turing", "Von Neumann" ] 

name_wanted = input("what name do you want to find?")

for index, name in enumerate(names):
    if name == name_wanted: 
        print(name_wanted, "is at position", index)
        break
