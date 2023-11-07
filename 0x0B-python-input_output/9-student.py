#!/usr/bin/python3
"""Student module."""


class Student():
    """Defines a Student."""

    def __init__(self, first_name, last_name, age):
        """Sets attributes for the Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary ."""
        return self.__dict__
