#!/usr/bin/python3
"""
Module that provides a Rectangle class inheriting from BaseGeometry.
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle class that inherits from BaseGeometry.

    This class represents a rectangle with width and height attributes.
    Both width and height must be positive integers.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle with width and height.

        Args:
            width (int): The width of the rectangle (must be positive)
            height (int): The height of the rectangle (must be positive)
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
