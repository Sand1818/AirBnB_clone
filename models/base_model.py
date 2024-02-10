#!/usr/bin/python3
"""
Defines the BaseModel class
"""
import uuid
from datetime import datetime
import models

class BaseModel():
    """BaseModel class of the Airbnb"""
    def __init__(self, *args, **kwargs):
        """Initialises BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns str representaion of BaseModel instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates to the current datetime updated_at"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns dictionary of BaseModel of instance"""
        sj_dict = self.__dict__.copy()
        sj_dict['__class__'] = self.__class__.__name__
        sj_dict['created_at'] = self.created_at.isoformat()
        sj_dict['updated_at'] = self.updated_at.isoformat()
        return sj_dict
