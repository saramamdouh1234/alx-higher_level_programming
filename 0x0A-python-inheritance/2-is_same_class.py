#!/usr/bin/python3
"""Defines a class."""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.

    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
