#!/usr/bin/python3
"""File storage class"""

import json
import os
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity


class FileStorage:
    """File storage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the ob with key <onj class name>.id"""
        self.__objects[f"{obj.__class__.__name__},{obj.id}"] = obj

    def save(self):
        """Serialise __objects to JSON"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deseialise JSON to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                loaded_dict = json.load(f)
            for value in loaded_dict.values():
                obj_class = value["__class__"]
                self.__objects["{}.{}".format(obj_class, value["id"])] = \
                    eval(obj_class)(**value)
