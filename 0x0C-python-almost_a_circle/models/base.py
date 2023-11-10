#!/usr/bin/python3
"""Module for base class"""

class Base:
    """A private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """If id is not None, assign it. Otherwise, increment __nb_objects"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

