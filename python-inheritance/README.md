# Python - Inheritance

This project covers Python inheritance concepts including:

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use isinstance, issubclass, type and super built-in functions

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

## Tasks

This project contains the following tasks:

1. **0-lookup.py** - Function that returns the list of available attributes and methods of an object
2. **1-my_list.py** - Class MyList that inherits from list with a print_sorted method
3. **2-is_same_class.py** - Function that checks if an object is exactly an instance of a specified class
4. **3-is_kind_of_class.py** - Function that checks if an object is an instance of or inherited from a specified class
5. **4-inherits_from.py** - Function that checks if an object is an instance of a class that inherited from a specified class
6. **5-base_geometry.py** - Empty class BaseGeometry
7. **6-base_geometry.py** - BaseGeometry class with area method that raises an exception
8. **7-base_geometry.py** - BaseGeometry class with area and integer_validator methods
9. **8-rectangle.py** - Rectangle class that inherits from BaseGeometry
10. **9-rectangle.py** - Rectangle class with area method and string representation
11. **10-square.py** - Square class that inherits from Rectangle
12. **11-square.py** - Square class with proper string representation 