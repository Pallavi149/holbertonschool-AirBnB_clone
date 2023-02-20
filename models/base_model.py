#!/usr/bin/python3
"""BaseModel Class"""
from datetime import datetime
import uuid


class BaseModel:
    """BaseModel of class"""
    def __init__(self, *args, **kwargs):
        """Initialise base model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return string form of class name, id and dict"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """update the update_at attribute with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Create dictionary with all instance attrributes, add class name as
        __clas__, convert created_at and updated_at attributes to string ISO
        format using isoformat()
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
