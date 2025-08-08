# Python OOP - Abstract Class, Interface, Subclassing

This project focuses on Object-Oriented Programming (OOP) concepts in Python, specifically covering abstract classes, interfaces, duck typing, and subclassing standard base classes.

## Learning Objectives

- **Abstract Classes**: Understand and apply abstract classes to define common interfaces while enforcing certain levels of class completeness.
- **Interfaces and Duck Typing**: Grasp the concept of interfaces and duck typing to ensure that objects adhere to a specific contract or protocol.
- **Subclassing Standard Base Classes**: Learn to extend standard base classes like lists, dictionaries, and iterators to create custom data structures with specialized behavior.
- **Method Overriding**: Employ method overriding to alter or enhance the behavior of base class methods.
- **Multiple Inheritance**: Understand and apply multiple inheritance to form complex relationships between classes.
- **Mixins**: Utilize mixins to compose behavior across unrelated classes.

## Resources

- [Python 3 Object-Oriented Programming](https://realpython.com/python3-object-oriented-programming/)
- [ABC — Abstract Base Classes](https://docs.python.org/3/library/abc.html)
- [Real Python - Object-Oriented Programming (OOP) in Python 3](https://realpython.com/python3-object-oriented-programming/)
- [Corey Schafer - OOP Playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)
- [sentdex - Python OOP Tutorial](https://www.youtube.com/playlist?list=PLQVvvaa0QuDfefDfXb1YJ4tMrT6ba81EL)

## Tasks

### 0. Abstract Animal Class and its Subclasses
Create an abstract class named `Animal` using the ABC package with an abstract method called `sound`. Implement two subclasses: `Dog` and `Cat` with their respective sound methods.

### 1. Shapes, Interfaces, and Duck Typing
Create an abstract class `Shape` with abstract methods `area` and `perimeter`. Implement `Circle` and `Rectangle` classes and a `shape_info` function that uses duck typing.

### 2. Extending the Python List with Notifications
Create a `VerboseList` class that extends Python's built-in `list` class and prints notifications for add/remove operations.

### 3. CountedIterator - Keeping Track of Iteration
Create a `CountedIterator` class that extends the built-in iterator and keeps track of the number of items iterated.

### 4. The Enigmatic FlyingFish - Exploring Multiple Inheritance
Create a `FlyingFish` class that inherits from both `Fish` and `Bird` classes, demonstrating multiple inheritance.

### 5. The Mystical Dragon - Mastering Mixins
Design `SwimMixin` and `FlyMixin` classes, then create a `Dragon` class that inherits from both mixins.

## Requirements

### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc

### Python Test Cases
- All your files should end with a new line
- All your test files should be inside a folder tests
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation
- All your classes should have a documentation
- All your functions (inside and outside a class) should have a documentation
- A documentation is not a simple word, it's a real sentence explaining what's the purpose of the module, class or method

## Files

- `task_00_abc.py` - Abstract Animal class with Dog and Cat subclasses
- `task_01_duck_typing.py` - Shape abstract class with Circle and Rectangle implementations
- `task_02_verboselist.py` - VerboseList class extending Python's list
- `task_03_countediterator.py` - CountedIterator class for tracking iterations
- `task_04_flyingfish.py` - FlyingFish class demonstrating multiple inheritance
- `task_05_dragon.py` - Dragon class using SwimMixin and FlyMixin 