#!/usr/bin/python3
"""
Functions to write to files
"""


def write_file(filename="", text=""):
    """
    write text to the file
    """
    with open(filename, mode="w", encoding="UTF8") as f:
        return f.write(text)
