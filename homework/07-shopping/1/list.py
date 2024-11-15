import json



def command_help(help_dict, help_name=None):
    if "main" in help_dict.keys():
        help_main = help_dict["main"]
        for command in help_main:
            help_command = help_main[command]
            print(f"{command}:\n  Description: {help_command['description']}\n  Usage: '{help_command['usage']}'\n")
    else:
        help_command = help_dict
        print(f"{help_name}:\n  Description: {help_command['description']}\n  Usage: '{help_command['usage']}'\n")



with open("help.json", "r") as f:
    help = json.load(f)
current_list = []
response = ""
options = list(help["main"].keys())



while response.lower() != "exit":
    response = input(f"\nWhat do you want to do? ({options})\n>> ")
    response_split = response.split(" ")
    if response_split[0] in options:

        if response_split[0] == "add":
            if len(response_split) > 1:
                current_list.append(response_split[1])
            else:
                print(f"Err: Please use correct arguments")
                print(f"     Run 'help add' for more information")

        if response_split[0] == "remove":
            if len(response_split) > 1:
                try:
                    current_list.remove(response_split[1])
                except ValueError:
                    print("Err: Item not in list")
            else:
                print(f"Err: Please use correct arguments")
                print(f"     Run 'help remove' for more information")

        if response_split[0] == "view":
            print(current_list)

        if response_split[0] == "help":
            if len(response_split) == 1:
                command_help(help)
            elif len(response_split) == 2:
                try:
                    command_help(help["main"][response_split[1]], response_split[1])
                except KeyError:
                    print("Err: Function does not exist")
            else:
                print(f"Err: Please use correct arguments")
                print(f"     Run 'help help' for more information")
    else:
        print("Please enter a valid command")
