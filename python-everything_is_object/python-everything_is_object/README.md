# Python - Everything is an object

This project explores Python's object model and how objects behave in different scenarios. It covers concepts like:

- Object identity and references
- Mutable vs immutable objects
- Aliasing and assignment
- Function parameter passing
- List operations and their effects on object identity

## Files

- `0-answer.txt` to `28-answer.txt`: Answer files for various Python object behavior questions
- `19-copy_list.py`: Function to create a copy of a list

## Key Concepts

### Objects and References
In Python, everything is an object. Variables are references to objects, not the objects themselves.

### Mutable vs Immutable
- **Immutable objects**: int, str, tuple, frozenset - cannot be changed after creation
- **Mutable objects**: list, dict, set - can be modified after creation

### Identity vs Equality
- `==` compares values (equality)
- `is` compares object identity (same object in memory)
- `id()` returns the object's memory address

### Function Parameters
Python passes arguments by object reference, which means:
- For immutable objects: changes inside functions don't affect the original
- For mutable objects: changes inside functions affect the original object
