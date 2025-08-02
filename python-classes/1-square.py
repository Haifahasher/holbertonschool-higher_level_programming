#!/usr/bin/python3
"""
Module containing a Square class with private size attribute.
"""


class Square:
    """
    A Square class that defines a square with a private size attribute.
    """

    def __init__(self, size):
        """
        Initialize a Square instance with a private size attribute.

        Args:
            size: The size of the square
        """
        self.__size = size
