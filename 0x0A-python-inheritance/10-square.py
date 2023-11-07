#!/usr/bin/python3
"""defines a class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """implements class """

    def __init__(self, size):
        """initilizing a new square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
