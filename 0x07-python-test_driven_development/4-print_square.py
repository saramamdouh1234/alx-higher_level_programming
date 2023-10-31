#!/usr/bin/python3
""" prints a square """ 


def print_square(size):
    """ prints a square with the character # """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for x in range(0, size):
        for y in range(size):
            print("#", end="")
        print("")
