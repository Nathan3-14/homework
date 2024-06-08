from main import print, console, Computer

#* All setup and calculations*#
test_computer = Computer(
    10,
    2
)
speed = test_computer.get_speed()
operation_count = 50
operation_time = operation_count / speed


#* Error of negative number *#
print("\n[dark_green]Enter the clock speed (Hz)[/dark_green]\n[green3]>>[/green3] -3")
print("[red]Err:[/red] [bright_cyan]Input was not positive float[/bright_cyan]")

print("\n[dark_green]Enter the clock speed (Hz)[/dark_green]\n[green3]>>[/green3] 10")


#* Error of non-int (float) *#
print("\n[dark_green]Enter the number of cores[/dark_green]\n[green3]>>[/green3] 0.4")
print("[red]Err:[/red] [bright_cyan]Input was not positive int[/bright_cyan]")

#* Error of non-int (string) *#
print("\n[dark_green]Enter the number of cores[/dark_green]\n[green3]>>[/green3] seven")
print("[red]Err:[/red] [bright_cyan]Input was not positive int[/bright_cyan]")

print("\n[dark_green]Enter the number of cores[/dark_green]\n[green3]>>[/green3] 2\n")


print(f"You can calculate [bright_yellow]{speed}[/bright_yellow] {"instructions" if speed > 1 else "instruction"} per second!")
print("\n[dark_green]How many operations are needed to be processed?[/dark_green]\n[green3]>>[/green3] 50")
print(f"Your computer will take {operation_time} {"seconds" if operation_time != 1 else "second"} to complete your operations")


console.save_svg("images/output.svg")