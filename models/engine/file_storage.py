#!/usr/bin/python3
"""
Serialized instances to a JSON file and deserializes
in JSON file to instances
"""
import json
from datetime import datetime


class FilestSorage:
    """
    FileStorage class
    """
    
    __file_path = "JSONstorage.json"
    __objects = {}
    
    def all(self):
        """
        Return the dictionary
        """
        return FilestSorage.__objects
    
    def new(self, obj):
        '''
        Sets in __objects the obj with key
        <obj class name>.id
        '''
        
        key = obj.to_dict()['__class__']+ "." + obj.id
        FilestSorage.__objects.update({key: obj})
        
    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        
        my_dict = {}
        my_dict.update(FilestSorage.__objects)
        for key, value in my_dict.items():
            my_dict[key] = value.to_dict()
        with open(FilestSorage.__file_path, "w+") as write_file:
            json.dump(my_dict, write_file)
    
    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        
        new_dict = {}
        try:
            from models.base_model import BaseModel
            with open(self.__file_path, "r") as read_file:
                new_dict = json.load(read_file)
                for key, value in new_dict.items():
                    FilestSorage.__objects[key] = BaseModel(**value)
        except IOError:
            pass