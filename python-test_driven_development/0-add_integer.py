#!/usr/bin/python3
"""
0-add_integer module.

Provides a single function add_integer(a, b=98) that
adds two integers (floats are cast to ints).
"""


def add_integer(a, b=98):
    """
    Add two integers a and b.

    Floats are truncated to ints before addition.

    Raises:
        TypeError: a must be an integer
        TypeError: b must be an integer

    Returns:
        int: the sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
