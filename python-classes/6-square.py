#!/usr/bin/python3
"""
This module defines a Square class with size validation.
"""


class Square:
    """a Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with an optional size."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """a getter function for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """a getter function for position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square."""
        if (
            type(value) is not tuple
            or len(value) != 2
            or type(value[0]) is not int
            or type(value[1]) is not int
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """a function that prints a # = to size"""
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for j in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
