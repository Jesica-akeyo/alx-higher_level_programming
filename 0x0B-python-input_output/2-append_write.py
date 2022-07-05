#!/usr/bin/python3
""" Module that contains a function that appends to a text file
"""


def append_write(filename="", text=""):
    """ Function that appends to a text file
    filename: file name
    text: text to write
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
