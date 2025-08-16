#!/usr/bin/env python3
"""
Pickling Custom Classes Module

This module demonstrates how to serialize and deserialize custom Python objects
using the pickle module.
"""

import pickle


class CustomObject:
    """
    A custom Python class that can be serialized and deserialized using pickle.

    Attributes:
        name (str): The name of the person
        age (int): The age of the person
        is_student (bool): Whether the person is a student
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        Args:
            name (str): The name of the person
            age (int): The age of the person
            is_student (bool): Whether the person is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes in a formatted way.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.

        Args:
            filename (str): The filename to save the serialized object to

        Returns:
            None
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Error serializing object: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance from a file using pickle.

        Args:
            filename (str): The filename to load the serialized object from

        Returns:
            CustomObject: The deserialized object, or None if an error occurs
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return None
        except pickle.UnpicklingError as e:
            print(f"Error unpickling object from '{filename}': {e}")
            return None
        except Exception as e:
            print(f"Error deserializing object: {e}")
            return None
