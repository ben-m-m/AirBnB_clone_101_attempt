#!/usr/bin/python3
"""class BaseModel defines all common attributes/methods for other classes"""


import uuid
import models
from datetime import datetime


class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel
        Args:
            *args
            **kwargs
        """
        if kwargs != {}:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    val = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, k, val)
                    continue
                if k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """returns string representation of the instance"""
        st = "[{:s}] ({:s}) {}"
        return st.format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        updates public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        new = dict(self.__dict__)
        new["__class__"] = type(self).__name__
        new["created_at"] = new["created_at"].isoformat()
        new["updated_at"] = new["updated_at"].isoformat()

        return new
