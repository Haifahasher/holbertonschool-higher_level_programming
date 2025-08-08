#!/usr/bin/python3
"""
Module that provides a CountedIterator class extending the built-in iterator.
This module demonstrates subclassing and tracking iteration progress.
"""


class CountedIterator:
    """
    A custom iterator class that extends the built-in iterator functionality.

    This class wraps an iterable and keeps track of how many items
    have been iterated over using the __next__ method.
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable.

        Args:
            iterable: An iterable object to iterate over
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Get the next item from the iterator and increment the counter.

        Returns:
            The next item from the iterator

        Raises:
            StopIteration: When there are no more items to iterate
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """
        Return self to make the CountedIterator iterable.

        Returns:
            self: The CountedIterator instance
        """
        return self

    def get_count(self):
        """
        Get the current count of items that have been iterated.

        Returns:
            int: The number of items that have been iterated so far
        """
        return self.count
