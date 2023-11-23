# Setup

## Requirements
- Rich (installed via [pip](code-snippets/#rich-install))

## Installation
- Clone this repo into your project folder
- Rename it to 'command'
- Inside that folder, create a json file and name it whatever you like (recommended is 'help.json')
- Copy [default.json](https://github.com/Nathan3-14/PythonCommandReader/blob/main/default.json) into your new file
- Add any function you wish to add following the template
- Note, the other files will not be used but will be automatically replaced by git upon an update to the interpreter


## Usage
- Import the module ([1](code-snippets/#import)) at the top of your script
- Add a 'command_dict' dictionary to store all your functions ([2](code-snippets/#command-dictionary))
- Create your command interpreter by assigning a variable with the CommandReader class ([3](code-snippets/#interpreter-variable))
- To run a command, use the run command, built in to the class ([4](code-snippets/#run-command))