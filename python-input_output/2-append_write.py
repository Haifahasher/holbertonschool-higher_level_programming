#!/usr/bin/python3
"""
Functions to append to files
"""


def append_write(filename="", text=""):
    """
    append text to the file
    """
    with open(filename, mode="a", encoding="UTF8") as f:
        return f.write(text)
