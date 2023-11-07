#!/usr/bin/python3
"""read_file module."""


def read_file(filename=""):
    """Reads a text file and prints it."""
    with open(filename, 'r') as f:
        print(f.read(), end='')
