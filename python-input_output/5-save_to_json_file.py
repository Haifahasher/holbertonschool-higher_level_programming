#!/usr/bin/python3
"""
Module for saving objects to JSON files
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation

    Args:
        my_obj: The object to serialize and save
        filename (str): The name of the file to write to
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
