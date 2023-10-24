#!/usr/bin/python3
"""
No module imported
"""


class Square:
    """
    class square
    """

    def __init__(self, size=0, position=(0, 0)):
        
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        self.__size = value
        try:
            assert type(value) == int
        except BaseException:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @position.setter
    def position(self, value):
        self.__position = value
        try:
            assert type(value) == tuple
        except BaseException:
            raise TypeError("position must be a tuple of 2 positive integers")
        try:
            assert type(value[0]) == int or type(value[1]) == int
        except BaseException:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        
        return self.__size * self.__size

    def my_print(self):
        """ print square """
        if self.size == 0:
            print()
        for i in range(self.position[1]):
            print("\n")
        for i in range(self.size):
            for x in range(self.position[0]):
                print(" ", end="")
            for x in range(self.size):
                print("#", end="")
            print()
