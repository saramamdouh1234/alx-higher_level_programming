#!/usr/bin/python3
"""append_write module."""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file returns the number.
    """
    with open(filename, 'a') as f:
        return f.write(text)
