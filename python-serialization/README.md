# Python Serialization

This project explores marshaling and serialization concepts in Python, demonstrating how to transform and communicate data between different parts of a system or across different systems.

## Learning Objectives

- Articulate the differences and similarities between marshaling and serialization
- Implement serialization in practical programming tasks
- Understand how serialized data can be used in web applications, databases, and network communications
- Evaluate the performance implications of different serialization formats

## Tasks

### 0. Basic Serialization
**File:** `task_00_basic_serialization.py`

A basic serialization module that adds functionality to serialize a Python dictionary to a JSON file and deserialize the JSON file to recreate the Python dictionary.

**Functions:**
- `serialize_and_save_to_file(data, filename)`: Serializes a Python dictionary to JSON and saves it to a file
- `load_and_deserialize(filename)`: Loads and deserializes JSON data from a file back to a Python dictionary

### 1. Pickling Custom Classes
**File:** `task_01_pickle.py`

Demonstrates how to serialize and deserialize custom Python objects using the pickle module.

**Class:** `CustomObject`
- **Attributes:** name (str), age (int), is_student (bool)
- **Methods:**
  - `display()`: Prints object attributes in a formatted way
  - `serialize(filename)`: Serializes the object to a file using pickle
  - `deserialize(filename)`: Class method to deserialize an object from a file

### 2. Converting CSV Data to JSON Format
**File:** `task_02_csv.py`

Gains experience in reading data from one format (CSV) and converting it into another format (JSON) using serialization techniques.

**Function:** `convert_csv_to_json(csv_filename)`
- Reads CSV data using DictReader
- Converts each row to a dictionary
- Serializes the list of dictionaries to JSON
- Saves the result to `data.json`

### 3. Serializing and Deserializing with XML
**File:** `task_03_xml.py`

Explores serialization and deserialization using XML as an alternative format to JSON.

**Functions:**
- `serialize_to_xml(dictionary, filename)`: Serializes a Python dictionary to XML format
- `deserialize_from_xml(filename)`: Deserializes XML data back to a Python dictionary

## Usage Examples

### Basic Serialization
```python
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

data = {"name": "John Doe", "age": 30, "city": "New York"}
serialize_and_save_to_file(data, 'data.json')
deserialized_data = load_and_deserialize('data.json')
```

### Pickling Custom Classes
```python
from task_01_pickle import CustomObject

obj = CustomObject(name="John", age=25, is_student=True)
obj.serialize("object.pkl")
new_obj = CustomObject.deserialize("object.pkl")
```

### CSV to JSON Conversion
```python
from task_02_csv import convert_csv_to_json

convert_csv_to_json("data.csv")
```

### XML Serialization
```python
from task_03_xml import serialize_to_xml, deserialize_from_xml

sample_dict = {'name': 'John', 'age': '28', 'city': 'New York'}
serialize_to_xml(sample_dict, "data.xml")
deserialized_data = deserialize_from_xml("data.xml")
```

## Resources

- [Real Python Serialization](https://realpython.com/python-serialization/)
- [Real Python: Working With JSON Data in Python](https://realpython.com/python-json/)
- [Python's pickle documentation](https://docs.python.org/3/library/pickle.html)
- [CSV to JSON in Python](https://realpython.com/python-csv/)
- [Python XML ElementTree Guide](https://docs.python.org/3/library/xml.etree.elementtree.html) 