#!/usr/bin/python3
"""
Module containing a Square class with position attribute.
"""


class Square:
    """
    A Square class that defines a square with size and position properties,
    area calculation, and print functionality.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square instance with optional size and position.

        Args:
            size: The size of the square (default: 0)
            position: The position of the square as a tuple of 2 positive
                     integers (default: (0, 0))

        Raises:
            TypeError: If size is not an integer or position is not a tuple
                     of 2 positive integers
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int) or not isinstance(position[1],
                                                             int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value: The new size value

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Get the position of the square.

        Returns:
            tuple: The position of the square as (x, y)
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square with validation.

        Args:
            value: The new position value as a tuple of 2 positive integers

        Raises:
            TypeError: If value is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square (size squared)
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the '#' character with position offset.
        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print()
        else:
            # Print vertical offset (position[1] lines of spaces)
            for _ in range(self.__position[1]):
                print()

            # Print the square with horizontal offset
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
