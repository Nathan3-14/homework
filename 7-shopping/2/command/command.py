import os
import platform
import json
from rich import print
from rich.prompt import Confirm


class CommandReader:
    def __init__(self, command_path: str, command_dict: list):
        with open(command_path, "r") as f:
            self.command_help = json.load(f)
            self.commands = command_dict.copy()
            self.commands["help"] = self.function_help
            self.commands["quit"] = self.function_quit

    def run(self, command_name: str, args: list):
        try:
            self.recent_command = self.commands[command_name](args)
            if self.recent_command == None:
                raise Exception("Check your function, make sure it returns a boolean")
            if not self.recent_command:
                print(f"[red]Err:[/red] Invalid function syntax. Run 'help {command_name}' for more information")
        except KeyError:
            print(f"[red]Err:[/red] Unrecognised function run 'help' for a list of functions")


    def help(self, command_name: str):
        self.temp_command_help = self.command_help["main"]
        if command_name == "main":
            for command in self.temp_command_help.keys():
                print(f"{command.capitalize()}:")
                print(f"  Description: {self.temp_command_help[command]['description']}")
                print(f"  Usage: {self.temp_command_help[command]['usage']}\n")
        else:
            self.temp_command_help = self.temp_command_help[command_name]
            print(f"{command_name.capitalize()}:")
            print(f"  Description: {self.temp_command_help['description']}")
            print(f"  Usage: {self.temp_command_help['usage']}\n")

    def function_help(self, args: list) -> bool:
        if len(args) == 1:
            self.help(args[0])
        elif len(args) == 0:
            self.help("main")
        else:
            return False
        return True

    def function_quit(self, args:list) -> bool:
        if len(args) > 0:
            return False
        quit()

class CommandLine:
    def __init__(self, interpreter: CommandReader):
        self.interpreter = interpreter
        if Confirm.ask("Clear the terminal before running?"):
            os.system("clear")
    
    def prompt(self):
        print(f"[green]user@{platform.node()}[/green] [blue]$[/blue] ", end="")
        self.response = input("")
        self.response_split = self.response.split(" ")
        self.interpreter.run(self.response_split[0], self.response_split[1:len(self.response_split)])
