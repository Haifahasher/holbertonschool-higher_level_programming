#!/usr/bin/python3
"""
Module that provides a Square class inheriting from Rectangle with proper
string representation.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A Square class that inherits from Rectangle.

    This class represents a square with a size attribute.
    The size must be a positive integer.
    """

    def __init__(self, size):
        """
        Initialize a Square with size.

        Args:
            size (int): The size of the square (must be positive)
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square (size * size)
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string in the format "[Square] <size>/<size>"
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
