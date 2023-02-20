#!/usr/bin/python3
"""Console class to"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    file = None

    # ----- basic hbnb commands -----
    def do_EOF(self, arg):
        """Quit the console"""
        return True

    def do_help(self, arg):
        """Use help commands"""
        super().do_help(arg)

    def do_quit(self, arg):
        """Quit the console"""
        return self.do_EOF('')

    def emptyline(self):
        """Do nothing on empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
