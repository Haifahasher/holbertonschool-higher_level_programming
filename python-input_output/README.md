# Python Input/Output

This project covers Python file handling, JSON serialization/deserialization, and object serialization concepts.

## Learning Objectives

- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the `with` statement
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure
- How to access command line parameters in a Python script

## Files

### File Operations
- `0-read_file.py` - Function to read a text file and print to stdout
- `1-write_file.py` - Function to write a string to a text file
- `2-append_write.py` - Function to append a string to a text file

### JSON Operations
- `3-to_json_string.py` - Function to convert object to JSON string
- `4-from_json_string.py` - Function to convert JSON string to object
- `5-save_to_json_file.py` - Function to save object to JSON file
- `6-load_from_json_file.py` - Function to load object from JSON file
- `7-add_item.py` - Script to add command line arguments to JSON file

### Object Serialization
- `8-class_to_json.py` - Function to convert class object to dictionary
- `9-student.py` - Student class with basic JSON serialization
- `10-student.py` - Student class with filtered JSON serialization
- `11-student.py` - Student class with full serialization/deserialization

### Algorithms
- `12-pascal_triangle.py` - Function to generate Pascal's triangle

## Usage Examples

### File Reading
```python
read_file = __import__('0-read_file').read_file
read_file("my_file.txt")
```

### File Writing
```python
write_file = __import__('1-write_file').write_file
nb_chars = write_file("output.txt", "Hello, World!")
```

### JSON Operations
```python
to_json_string = __import__('3-to_json_string').to_json_string
my_dict = {"name": "John", "age": 30}
json_str = to_json_string(my_dict)
```

### Student Class
```python
Student = __import__('9-student').Student
student = Student("John", "Doe", 23)
json_data = student.to_json()
```

### Pascal's Triangle
```python
pascal_triangle = __import__('12-pascal_triangle').pascal_triangle
triangle = pascal_triangle(5)
```

## Requirements

- Python 3.8.5
- All files must be executable
- Code must follow pycodestyle (version 2.7.*)
- All files must end with a new line
- First line of all files must be `#!/usr/bin/python3` 