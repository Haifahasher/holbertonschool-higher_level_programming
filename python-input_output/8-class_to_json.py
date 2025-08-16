#!/usr/bin/python3
"""
Functions to save a class object
"""


def class_to_json(obj):
    """
    return obj as a string
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("Object has no __dict__ to serialize")

    parts = []
    for key, value in obj.__dict__.items():
        if isinstance(value, str):
            parts.append(f"'{key}': '{value}'")
        elif isinstance(value, (int, float, bool)):
            parts.append(f"'{key}': {str(value)}")
        elif value is None:
            parts.append(f"'{key}': null")
        elif hasattr(value, "__dict__"):
            # Recursively handle nested objects
            parts.append(f"'{key}': {class_to_json(value)}")
        else:
            # Fallback: turn into string
            parts.append(f"'{key}': '{value}'")
    # return "{" + ", ".join(parts) + "}"
    return obj.__dict__
