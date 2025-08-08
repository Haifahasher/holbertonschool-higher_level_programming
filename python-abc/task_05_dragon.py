#!/usr/bin/python3
"""
Module that provides SwimMixin, FlyMixin, and Dragon classes
demonstrating mixins. This module shows how mixins can be used to
compose behavior across classes.
"""


class SwimMixin:
    """
    A mixin class that provides swimming behavior.

    Mixins are classes that are not meant to be instantiated on their
    own, but are designed to be combined with other classes to add
    functionality.
    """

    def swim(self):
        """
        Print a message indicating the creature is swimming.
        """
        print("The creature swims!")


class FlyMixin:
    """
    A mixin class that provides flying behavior.

    Mixins are classes that are not meant to be instantiated on their
    own, but are designed to be combined with other classes to add
    functionality.
    """

    def fly(self):
        """
        Print a message indicating the creature is flying.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that inherits from both SwimMixin and FlyMixin.

    This class demonstrates how mixins can be combined to create
    complex behavior by inheriting from multiple mixin classes.
    The Dragon can both swim and fly, and also has its own unique
    roar ability.
    """

    def roar(self):
        """
        Print a message indicating the dragon is roaring.
        """
        print("The dragon roars!")
