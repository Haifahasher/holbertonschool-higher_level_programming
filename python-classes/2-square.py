#!/usr/bin/python3
"""Module that defines a Square class with size validation."""


class Square:
    """Represents a square with a size attribute."""

    def __init__(self, size=0):
        """Initializes a Square with a given size.

        Args:
            size (int): Size of the square, must be an integer >= 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
