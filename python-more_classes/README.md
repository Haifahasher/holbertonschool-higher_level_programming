# Python More Classes

This project covers advanced Object-Oriented Programming (OOP) concepts in Python, including special methods, class attributes, static methods, and class methods.

## Learning Objectives

### General OOP Concepts

**Why Python programming is awesome:**
- Simple and readable syntax
- Extensive standard library
- Strong community support
- Versatile applications (web, data science, AI, etc.)
- Dynamic typing and high-level abstractions

**What is OOP:**
Object-Oriented Programming is a programming paradigm that organizes code into objects containing data and behavior, promoting code reuse and maintainability.

**"First-class everything":**
In Python, everything is an object - functions, classes, modules, even numbers and strings can be assigned to variables, passed as arguments, and stored in data structures.

**What is a Class:**
A blueprint or template that defines the structure and behavior of objects.

**What is an Object and Instance:**
- **Object**: An instance of a class containing data and behavior
- **Instance**: A specific occurrence of a class (synonymous with object)

**Difference between Class and Object/Instance:**
- **Class**: Template/blueprint defining structure and behavior
- **Object/Instance**: Concrete example created from the class template

**What is an Attribute:**
A variable that belongs to an object or class, storing data associated with the object.

**Public, Protected, and Private Attributes:**
- **Public**: Accessible from anywhere (no prefix)
- **Protected**: Conventionally private (single underscore prefix)
- **Private**: Name-mangled (double underscore prefix)

**What is self:**
A reference to the current instance of the class, used to access attributes and methods.

**What is a Method:**
A function that belongs to a class and operates on the object's data.

**Special __init__ method:**
A constructor automatically called when creating a new instance, initializing object attributes.

**Data Abstraction, Encapsulation, and Information Hiding:**
- **Data Abstraction**: Hiding complex implementation details
- **Data Encapsulation**: Bundling data and methods in a single unit
- **Information Hiding**: Restricting access to prevent direct manipulation

**What is a Property:**
A special attribute using getter and setter methods to control access to instance variables.

**Attribute vs Property:**
- **Attribute**: Direct access to instance variables
- **Property**: Controlled access through getter/setter methods

**Pythonic Getters and Setters:**
Using `@property` decorator for getters and `@attribute.setter` for setters.

**Special __str__ and __repr__ methods:**
- **__str__**: User-friendly string representation
- **__repr__**: Developer-friendly string representation for debugging

**Difference between __str__ and __repr__:**
- **__str__**: For end users, readable format
- **__repr__**: For developers, should contain enough info to recreate object

**What is a Class Attribute:**
A variable shared by all instances of a class, defined at the class level.

**Object Attribute vs Class Attribute:**
- **Object Attribute**: Belongs to individual instances
- **Class Attribute**: Shared by all instances of the class

**What is a Class Method:**
A method that operates on the class itself, using `@classmethod` decorator and `cls` parameter.

**What is a Static Method:**
A method that doesn't access class or instance data, using `@staticmethod` decorator.

**Dynamic Attribute Creation:**
Attributes can be added to instances dynamically using dot notation or `setattr()`.

**Attribute Binding:**
Attributes can be bound to objects and classes using assignment or `setattr()`.

**__dict__ Attribute:**
Contains a dictionary of the object's attributes and their values.

**Attribute Lookup:**
Python follows Method Resolution Order (MRO): instance → class → parent classes.

**getattr Function:**
`getattr(object, name[, default])` retrieves the value of a named attribute.

## Files in this Project

- `0-rectangle.py`: Empty Rectangle class
- `1-rectangle.py`: Rectangle class with width/height properties
- `2-rectangle.py`: Rectangle class with area and perimeter methods
- `3-rectangle.py`: Rectangle class with string representation
- `4-rectangle.py`: Rectangle class with eval-compatible repr
- `5-rectangle.py`: Rectangle class with destructor
- `6-rectangle.py`: Rectangle class with instance counter
- `7-rectangle.py`: Rectangle class with customizable print symbol
- `8-rectangle.py`: Rectangle class with static comparison method
- `9-rectangle.py`: Rectangle class with class method for squares

## Requirements

- All files must be executable
- All files must end with a new line
- All files must start with `#!/usr/bin/python3`
- All modules, classes, and functions must have documentation
- Code must follow pycodestyle guidelines 