#!/usr/bin/python3
"""
Module that provides a BaseGeometry class with area and integer_validator
methods.
"""


class BaseGeometry:
    """
    A base geometry class with area and integer validation methods.

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

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Args:
            name (str): The name of the value being validated
            value: The value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
