import cmd 

class TodoCLI(cmd.Cmd):

    prompt = '>>> '
    intro = "Welcome to your todo list CLI tool. Type 'help' for available commands."