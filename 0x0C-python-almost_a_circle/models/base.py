#!/usr/bin/python3
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @property
    def nb_objects(self):
        return self.__nb_objects

    @nb_objects.setter
    def nb_objects(self, value):
        self.__nb_objects = value

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        js = ""
        ls = []
        for i in list_objs:
            dic = i.to_dictionary()
            ls.append(dic)
        js += i.to_json_string(ls)
        with open(cls.__name__ + ".json", mode='w') as f:
            f.write(js)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy
