#!/usr/bin/python3
"""
This module contains functions to serialize python dictionaries to json
files
"""
import json


def serialize_and_save_to_file(data, filename):
    with open(filename, mode="w", encoding="UTF8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    with open(filename, mode="r", encoding="UTF8") as f:
        return json.load(f)
