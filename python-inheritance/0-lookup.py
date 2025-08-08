#!/usr/bin/python3
"""
Module that provides a function to list all attributes and methods of an
object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect

    Returns:
        list: A list containing all available attributes and methods of the
        object
    """
    return dir(obj)
