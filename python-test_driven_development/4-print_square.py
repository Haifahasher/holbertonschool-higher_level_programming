#!/usr/bin/python3
"""
4-print_square module.

Provides print_square(size) which prints
a square of '#' characters of side length size.
"""


def print_square(size):
    """
    Print a square of '#' characters of side length size.

    Args:
        size (int): the length of the square's side.

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
