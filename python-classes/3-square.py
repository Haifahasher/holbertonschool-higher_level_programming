#!/usr/bin/python3
"""
Module containing a Square class with area method.
"""


class Square:
    """
    A Square class that defines a square with size validation and area
    calculation.
    """

    def __init__(self, size=0):
        """
        Initialize a Square instance with optional size and validation.

        Args:
            size: The size of the square (default: 0)

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square (size squared)
        """
        return self.__size ** 2
