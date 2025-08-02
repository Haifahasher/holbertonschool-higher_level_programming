# Python Classes

This project covers Object-Oriented Programming (OOP) concepts in Python, including classes, objects, attributes, methods, and encapsulation.

## Concepts Covered

### What is OOP?
Object-Oriented Programming is a programming paradigm that organizes code into objects that contain data and code. It provides a way to structure programs so that properties and behaviors are bundled into individual objects.

### "First-class everything"
In Python, everything is an object - functions, classes, modules, even numbers and strings. This means they can be assigned to variables, passed as arguments, returned from functions, and stored in data structures.

### What is a Class?
A class is a blueprint or template for creating objects. It defines the attributes and methods that the objects will have.

### What is an Object and Instance?
- **Object**: An instance of a class that contains data and behavior
- **Instance**: A specific occurrence of a class (synonymous with object)

### Difference between Class and Object/Instance
- **Class**: A template/blueprint that defines structure and behavior
- **Object/Instance**: A concrete example created from the class template

### What is an Attribute?
An attribute is a variable that belongs to an object or class. It stores data associated with the object.

### Public, Protected, and Private Attributes
- **Public**: Accessible from anywhere (no prefix)
- **Protected**: Conventionally private, accessible but not intended for external use (single underscore prefix)
- **Private**: Name-mangled, not directly accessible from outside the class (double underscore prefix)

### What is self?
`self` is a reference to the current instance of the class. It's used to access attributes and methods of the object.

### What is a Method?
A method is a function that belongs to a class and operates on the object's data.

### Special __init__ Method
The `__init__` method is a constructor that is automatically called when creating a new instance. It initializes the object's attributes.

### Data Abstraction, Encapsulation, and Information Hiding
- **Data Abstraction**: Hiding complex implementation details and showing only necessary features
- **Data Encapsulation**: Bundling data and methods that operate on that data within a single unit
- **Information Hiding**: Restricting access to certain components to prevent direct manipulation

### What is a Property?
A property is a special kind of attribute that uses getter and setter methods to control access to instance variables.

### Attribute vs Property
- **Attribute**: Direct access to instance variables
- **Property**: Controlled access through getter/setter methods

### Pythonic Getters and Setters
Python uses the `@property` decorator to create getters and `@attribute.setter` to create setters, providing a clean interface for attribute access.

### Dynamic Attribute Creation
Attributes can be added to instances dynamically using dot notation or the `setattr()` function.

### Attribute Binding
Attributes can be bound to objects and classes using assignment or the `setattr()` function.

### __dict__ Attribute
The `__dict__` attribute contains a dictionary of the object's attributes and their values.

### Attribute Lookup
Python follows the Method Resolution Order (MRO) to find attributes: instance → class → parent classes.

### getattr Function
`getattr(object, name[, default])` retrieves the value of a named attribute of an object.

## Files in this Project

- `0-square.py`: Empty Square class
- `1-square.py`: Square class with private size attribute
- `2-square.py`: Square class with size validation
- `3-square.py`: Square class with area method
- `4-square.py`: Square class with size property
- `5-square.py`: Square class with print method
- `6-square.py`: Square class with position attribute

## Requirements

- All files must be executable
- All files must end with a new line
- All files must start with `#!/usr/bin/python3`
- All modules, classes, and functions must have documentation
- Code must follow pycodestyle guidelines 