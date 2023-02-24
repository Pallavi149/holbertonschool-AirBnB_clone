#!/usr/bin/python3
"""Console class to"""
import cmd
import shlex
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """Class that has basic commands for hbnb console"""

    prompt = '(hbnb) '

# ---Basic hbnb commands---

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

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it to the JSON file,
        and print the id. Ex: $ create BaseModel
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = eval(arg)
        except NameError:
            print("** class doesn't exist **")
            return
        instance = cls()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Prints string representation of an instance based on the class
        name and id."""
        args = shlex.split(arg)
        db = storage.all()
        if not len(args):
            print("** class name missing **")
        if args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in db:
            print("** no instance found **")
        else:
            print(db["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    storage.all().pop(key)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, args):
        """Prints all string representation of all instances based or not on
        the class name.
        """
        objs = []
        if not args:
            for obj in storage.all().values():
                objs.append(str(obj))
        else:
            args = args.split()
            if args[0] not in classes:
                print("** class doesn't exist **")
                return
            for key in storage.all():
                if args[0] in key:
                    objs.append(str(storage.all()[key]))
        print(objs)

    def do_update(self, arg):
        """Update an isntance based on the class name and id by adding or
        updating attribute (save the change/s into JSON file)
        Usage: update <class_name> <id> <attribute name> "<attribute value>
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        attr_name = args[2]
        try:
            value = type(getattr(obj, attr_name))(args[3])
        except Exception:
            value = args[3]
        setattr(obj, attr_name, value)
        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
