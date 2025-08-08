#!/usr/bin/python3
"""
Module that provides a MyList class inheriting from the built-in list class.
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    This class extends the functionality of the standard list by adding
    a method to print the list in sorted order without modifying the
    original list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.

        This method creates a sorted copy of the list and prints it,
        leaving the original list unchanged.
        """
        sorted_list = sorted(self)
        print(sorted_list)
