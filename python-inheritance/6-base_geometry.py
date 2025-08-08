#!/usr/bin/python3
"""
Module that provides a BaseGeometry class with an area method that raises
an exception.
"""


class BaseGeometry:
    """
    A base geometry class with an area method that raises an exception.

    This class serves as a foundation for geometry-related classes.
    The area method is meant to be overridden by subclasses.
    """

    def area(self):
        """
        Raises an Exception indicating that area() is not implemented.

        This method is meant to be overridden by subclasses to provide
        specific area calculation implementations.

        Raises:
            Exception: Always raises an exception with the message
            "area() is not implemented"
        """
        raise Exception("area() is not implemented")
