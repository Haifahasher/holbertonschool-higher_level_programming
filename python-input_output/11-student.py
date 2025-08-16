#!/usr/bin/python3
"""
Class student module
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        return {
                    k: v for k, v in self.__dict__.items()
                    if attrs is None or k in attrs
                    }

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
