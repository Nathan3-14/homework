from command.command import CommandReader
import platform
from rich import print
from rich.prompt import Confirm
import os

def function_add(args: list):
    if len(args) != 1:
        return False
    current_list.append(args[0])
    return True
    

def function_remove(args: list):
    if len(args) != 1:
        return False
    try:
        current_list.remove(args[0])
    except:
        print(f"Err: No item named '{args[0]}' in shopping list")
    return True

def function_view(args: list):
    if len(args) != 0:
        return False
    print(current_list)
    return True

command_dict = {
    "add": function_add,
    "remove": function_remove,
    "view": function_view
}

interpreter = CommandReader("./command/help.json", command_dict)
current_list = []

if Confirm.ask("Clear the terminal before running?"):
    os.system("clear")

print(f"Welcome to List!")
print(f"Run help for a list of commands\n")
while True:
    print(f"[green]user@{platform.node()}[/green] [blue]$[/blue] ", end="")
    response = input("")
    response_split = response.split(" ")
    interpreter.run(response_split[0], response_split[1:len(response_split)])