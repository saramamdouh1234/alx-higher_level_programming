#!/usr/bin/python3
"""write_file module."""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns number .
    """
    with open(filename, 'w') as f:
        return f.write(text)
