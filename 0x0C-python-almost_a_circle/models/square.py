#!/usr/bin/python3
""" class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes inst """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str method """
        str_square = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_square + str_id + str_xy + str_wh
    
    @property
    def size(self):
        """ size square """
        return self.width

    @size.setter
    def size(self, value):
        """setter size"""
        self.widht = value
        self.hight = value
