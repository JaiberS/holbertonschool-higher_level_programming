#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) == list:
            jdict = {}
            nwdict = self.__dict__
            for i in attrs:
                if type(i) != str:
                    return self.__dict__
                if i in nwdict:
                    jdict.setdefault(i, self.__dict__[i])
            return jdict
        return self.__dict__
