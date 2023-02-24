#!/usr/bin/python3
"""Console class to"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class that has basic commands for hbnb console"""

    prompt = '(hbnb) '

    current__Classes = {
        BaseModel.__name__: BaseModel,
        # User.__name__: User,
        #State.__name__: State,
        #City.__name__: City,
        #Place.__name__: Place,
        #Amenity.__name__: Amenity,
        #Review.__name__: Review
    }

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
        argus = shlex.split(arg)
        db = storage.all()

        if len(argus) < 1:
            print("** class name missing **")
        elif argus[0] not in HBNBCommand.current__Classes:
            print("** class doesn't exist **")
        elif len(argus) < 2:
            print("** instance id missing **")
        else:
            key = '{}.{}'.format(argus[0], argus[1])
            instance = db.get(key, None)
            if instance is None:
                print("** no instance found **")
            else:
                print(instance)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] in storage.__class__.__name__:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        storage.all().pop(key)
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not
        on the class name."""
        if not arg:
            print([str(obj) for obj in storage.all().values()])
        else:
            try:
                cls = eval(arg)
            except NameError:
                print("** class doesn't exist **")
                return
            print([str(obj) for obj in storage.all().values()])

    def do_update(self, arg):
        """Update an isntance based on the class name and id by adding or
        updating attribute (save the change/s into JSON file)
        Usage: update <class_name> <id> <attribute name> "<attribute value>
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] in storage.__class__.__name__:
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
