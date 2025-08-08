#!/usr/bin/python3
"""
Module that provides a VerboseList class extending Python's built-in list.
This module demonstrates subclassing standard base classes and method
overriding.
"""


class VerboseList(list):
    """
    A custom list class that extends Python's built-in list.

    This class overrides list modification methods to print notification
    messages when items are added or removed from the list.
    """

    def append(self, item):
        """
        Add an item to the end of the list and print a notification.

        Args:
            item: The item to add to the list
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list with items from an iterable and print a
        notification.

        Args:
            iterable: An iterable containing items to add to the list
        """
        original_length = len(self)
        super().extend(iterable)
        items_added = len(self) - original_length
        print(f"Extended the list with [{items_added}] items.")

    def remove(self, item):
        """
        Remove the first occurrence of an item from the list and print
        a notification.

        Args:
            item: The item to remove from the list
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Remove and return an item at the given index and print a
        notification.

        Args:
            index (int): The index of the item to remove (default: -1,
            last item)

        Returns:
            The item that was removed from the list
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
