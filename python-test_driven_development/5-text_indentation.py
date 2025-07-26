#!/usr/bin/python3
"""
5-text_indentation module.

Provides text_indentation(text) that prints a text with
two newlines after each occurrence of '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Print a text with two new lines after each '.', '?', or ':'.

    Args:
        text (str): the input text.

    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    i = 0

    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print()
            print()
            while i + 1 < len(text) and text[i + 1] in " \t":
                i += 1
        i += 1
