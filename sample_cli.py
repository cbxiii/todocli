import cmd

class MyCLI(cmd.Cmd):
    
    prompt = '>> '
    intro = "Welcome to myCLI. Type 'help' for available commands."

    def do_help(self, arg):
        """Show all commands."""
        print('''
            hello - prints a greeting.
            quit - quit the CLI.
        ''')

    def do_hello(self, line):
        """Print a greeting."""
        print("Hello world!")

    def do_quit(self, line):
        """Exit the CLI."""
        return True
    
if __name__ == "__main__":
    MyCLI().cmdloop()