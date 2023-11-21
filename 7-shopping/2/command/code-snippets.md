# Code snippets

## Import
```python
import command.command
```

## Command Dictionary
```python
# ...

def foo(args: list):
    print("Foo")
    return True
def bar(args: list):
    print("Bar")
    return True

command_dict = {
    "foo": foo,
    "bar": bar
}
# Remember to not call () the functions, just type their names #

# ...
```

## Interpreter Variable
```python
command_base = command.CommandReader("./command/help.json", command_dict)
# replace with the path to your help file  ^^^^^
```

## Run Command
```python
command_base.run("command_name", args)
# Args must be a list containing all arguments for the function
```

## Function Template
```python
def func_name(args: list): # Arguments must be (args: list) and nothing else
    if len(args) != 0: # If input args are incorrect
        return False # Used by the interpreter in order to show syntax errors
    do_stuff()
    return True # Is needed at the end of functions
```
