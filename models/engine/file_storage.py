#!/usr/bin/python3
"""
Serialized instances to a JSON file and deserializes
in JSON file to instances
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    FileStorage class
    """

    __file_path = "file.json"
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "Amenity": Amenity, "City": City, "Review": Review,
                  "State": State}

    def all(self):
        """
        Return the dictionary
        """
        return self.__objects

    def new(self, obj):
        '''
        Sets in __objects the obj with key
        <obj class name>.id
        '''

        key = obj.to_dict()['__class__'] + "." + obj.id
        FileStorage.__objects.update({key: obj})

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """

        my_dict = {}
        my_dict.update(self.__objects)
        for key, value in my_dict.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, "w+") as write_file:
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
                    obj = self.class_dict[value['__class__']](**value)
                    self.__objects[key] = obj
        except IOError:
            pass
