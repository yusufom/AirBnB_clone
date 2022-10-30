#!/usr/bin/python3
"""
    This module defines the BaseModel class and is a
    class from which all other classes would inherit
"""
from uuid import uuid4
from datetime import datetime
import json
import models.storage


class BaseModel:
    """
        The base class for all other classes created
        in this project..
    """

    def __init__(self, *args, **kwargs):
        
        if kwargs:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                elif k == 'created_at':
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    self.created_at = v
                elif k == 'updated_at':
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    self.updated_at = v
                else:
                    if k != "__class__":
                        self.__dict__[k] = v
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            storage.new()

    def __str__(self):
        """Define the print() representation of the BaseModel"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates the attribute 'update_at' with the current datetime"""
        self.updated_at = self.updated_at.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing key/value pairs of __dict__"""
        s_created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        s_updated_at = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.__dict__['created_at'] = s_created_at
        self.__dict__['updated_at'] = s_updated_at
        self.__dict__['__class__'] = type(self).__name__

        return (self.__dict__)
