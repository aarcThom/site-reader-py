import cmd
from mr_sid import test_sid

class MyCLI(cmd.Cmd):
    prompt = '>> '
    intro = test_sid()

    def do_hello(self, line):
        """Print a greeting."""
        print("Hello, World!")

    def do_quit(self, line):
        """Exit the CLI."""
        return True


def main():
    MyCLI().cmdloop()
    

if __name__ == "__main__":
    main()