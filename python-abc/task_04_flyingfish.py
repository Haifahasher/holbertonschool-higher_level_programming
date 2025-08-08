#!/usr/bin/python3
"""
Module that provides Fish, Bird, and FlyingFish classes demonstrating
multiple inheritance. This module shows how multiple inheritance works
and method resolution order (MRO).
"""


class Fish:
    """
    A class representing a fish with swimming and habitat behaviors.

    This class serves as one of the parent classes for FlyingFish,
    demonstrating multiple inheritance.
    """

    def swim(self):
        """
        Print a message indicating the fish is swimming.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Print a message indicating the fish's habitat.
        """
        print("The fish lives in water")


class Bird:
    """
    A class representing a bird with flying and habitat behaviors.

    This class serves as one of the parent classes for FlyingFish,
    demonstrating multiple inheritance.
    """

    def fly(self):
        """
        Print a message indicating the bird is flying.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Print a message indicating the bird's habitat.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A class representing a flying fish that inherits from both Fish and
    Bird.

    This class demonstrates multiple inheritance by combining behaviors
    from both Fish and Bird classes, and overriding methods to provide
    specialized behavior.
    """

    def fly(self):
        """
        Override the fly method to provide specialized flying behavior.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Override the swim method to provide specialized swimming behavior.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Override the habitat method to describe the flying fish's unique
        habitat.
        """
        print("The flying fish lives both in water and the sky!")
