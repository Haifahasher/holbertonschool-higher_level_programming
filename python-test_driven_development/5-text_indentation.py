#!/usr/bin/python3
"""
5-text_indentation module.

Provides text_indentation(text) that prints text with two new lines
after each occurrence of '.', '?' and ':' characters.
"""


def text_indentation(text):
    """
    Print text with two newlines after '.', '?' and ':' characters.

    Args:
        text (str): the input text to process.

    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buffer = ""
    length = len(text)
    i = 0

    while i < length:
        char = text[i]
        buffer += char
        if char in '.?:':
            # print the buffered sentence, stripped
            print(buffer.strip())
            print()
            buffer = ""
            # skip spaces immediately after punctuation
            i += 1
            while i < length and text[i] == ' ':
                i += 1
            continue
        i += 1

    # print any remaining text
    if buffer:
        print(buffer.strip())
