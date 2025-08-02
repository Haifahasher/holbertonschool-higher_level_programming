#!/usr/bin/python3
"""
This module defines an empty Rectangle  class.
"""


class Rectangle:
    """Represents an empty Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """a getter function for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """a getter function for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
