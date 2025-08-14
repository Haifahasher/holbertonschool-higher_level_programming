#!/usr/bin/python3
"""
Module for converting class objects to JSON-serializable dictionaries
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure for JSON serialization of an object

    Args:
        obj: An instance of a Class

    Returns:
        dict: A dictionary representation of the object's attributes
    """
    return obj.__dict__
