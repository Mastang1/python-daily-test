from pyreadline3 import Readline
readline = Readline()
global commands
commands = ['apple', 'app', 'application', 'bool', 'bootloaer', 'bricks']

def completer(text, state):
    options = [i for i in commands if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None
    
readline.set_completer(completer)
readline.parse_and_bind("tab: complete")


while True:
    line = readline.readline('Prompt> ')
    print(' --:\n', line)
    if 'quit' in line:
        break
