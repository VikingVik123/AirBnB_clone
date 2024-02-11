#!/usr/bin/python3
import json

"""
Defines the filestorage
"""

class FileStorage:
    """
    Creates a class called Filestorage
    """
    __file_path = "file.json"
    __obj = {}

    def all(self):
        """
        Returns the dictionary object
        """

        return self.__obj

    def new(self, obj):
        """Sets in __obj the obj with key <obj class name>.id"""

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__obj[key] = obj

    def save(self):
        """
        Serializes the object to json
        """
        serialized_obj = {}

        for key, obj in self.__obj.items():
            serialized_obj[key] = obj.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(serialized_obj, f)

    def reload(self):
        """
        Deserializes the json to objects
        """
       
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
            for key, obj_dict in data.items():
                class_name, obj_id = key.split('.')
                obj_class = getattr(__import__('models'), class_name)
                self.__obj[key] = obj_class(**obj_dict)
       
        except FileNotFoundError:
            pass

storage = FileStorage()

