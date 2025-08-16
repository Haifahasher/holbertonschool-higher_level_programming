#!/usr/bin/env python3
"""
Basic Serialization Module

This module provides functionality to serialize Python dictionaries to JSON files
and deserialize JSON files back to Python dictionaries.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data: A Python Dictionary with data
        filename: The filename of the output JSON file

    Returns:
        None
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error serializing data: {e}")


def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file.

    Args:
        filename: The filename of the input JSON file

    Returns:
        A Python Dictionary with the deserialized JSON data from the file
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from '{filename}': {e}")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
