#!/usr/bin/python3
"""
Module that provides an abstract Animal class and its concrete subclasses.
This module demonstrates the use of Abstract Base Classes (ABC) in Python.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    An abstract base class representing an animal.

    This class defines the interface that all animal subclasses must
    implement. It cannot be instantiated directly and serves as a
    blueprint for derived classes.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses.

        Returns:
            str: The sound that the animal makes
        """
        pass


class Dog(Animal):
    """
    A concrete subclass of Animal representing a dog.

    This class implements the abstract sound method defined in the
    Animal class.
    """

    def sound(self):
        """
        Returns the sound that a dog makes.

        Returns:
            str: "Bark" - the sound a dog makes
        """
        return "Bark"


class Cat(Animal):
    """
    A concrete subclass of Animal representing a cat.

    This class implements the abstract sound method defined in the
    Animal class.
    """

    def sound(self):
        """
        Returns the sound that a cat makes.

        Returns:
            str: "Meow" - the sound a cat makes
        """
        return "Meow"
