#!/usr/bin/python3
"""
Module defining a Student class with filtered JSON representation
"""


class Student:
    """
    A class that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance

        Args:
            first_name (str): The student's first name
            last_name (str): The student's last name
            age (int): The student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance

        Args:
            attrs (list): A list of strings representing attribute names to include

        Returns:
            dict: A dictionary representation of the Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items() if key in attrs}
