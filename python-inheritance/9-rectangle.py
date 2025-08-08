#!/usr/bin/python3
"""
Module that provides a Rectangle class inheriting from BaseGeometry with
area calculation.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height)
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string in the format "[Rectangle] <width>/<height>"
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
