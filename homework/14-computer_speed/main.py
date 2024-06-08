import sys
from rich.console import Console



console = Console(record=True)
print = console.print



#* Better input methods *#
def rinput(message: str) -> str: #? Used the rich text library to improve input's messages
    print(message, end="")
    return input()

def pfinput(message: str): #? Only allows positive floats to be entered
    def error():
        print("[red]Err:[/red] [bright_cyan]Input was not positive float[/bright_cyan]")
        pfinput(message)
    
    _input = rinput(message)
    try:
        _input_float = float(_input)
    except ValueError:
        error()
    
    if _input_float < 0:
        error()

    return _input_float

def piinput(message: str) -> int: #? Only allows positive integers to be entered
    def error():
        print("[red]Err:[/red] [bright_cyan]Input was not positive int[/bright_cyan]")
        piinput(message)

    _input = rinput(message)
    try:
        _input_int = int(_input)
    except ValueError:
        error()
    
    if _input_int < 0:
        error()

    return _input_int



#* Computer Code *#
class Computer:
    def __init__(self, clock_speed: float, number_of_cores: int) -> None:
        self.clock = clock_speed
        self.cores = number_of_cores
    
    def get_speed(self) -> float:
        return self.clock * self.cores



#* Main code *#
def run_computer():
    test_computer = Computer(
        pfinput("\n[dark_green]Enter the clock speed (Hz)[/dark_green]\n[green3]>>[/green3] "),
        piinput("\n[dark_green]Enter the number of cores[/dark_green]\n[green3]>>[/green3] ")
    ) #? Sets up a computer with the clock speed and cores as positive integers


    speed = test_computer.get_speed() #? Returns clock speed * number of cores
    print(f"You can calculate [bright_yellow]{speed}[/bright_yellow] {"instructions" if speed > 1 else "instruction"} per second!")


    operation_count = piinput("\n[dark_green]How many operations are needed to be processed?[/dark_green]\n[green3]>>[/green3] ")

    operation_time = operation_count / speed
    print(f"Your computer will take {operation_time} {"seconds" if operation_time != 1 else "second"} to complete your operations")



def main():
    run_computer()



if __name__ == "__main__":
    main()
