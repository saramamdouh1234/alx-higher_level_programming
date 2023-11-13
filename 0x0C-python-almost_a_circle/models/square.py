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

    def __str__(self):
        """ str  method """
        str_rectangle = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.size)

        return str_rectangle + str_id + str_xy + str_size

    def update(self, *args, **kwargs):
        """ update method """
        if args is not None and len(args) is not 0:
            list_str = ['id', 'size', 'x', 'y']
            for j in range(len(args)):
                if list_str[j] == 'size':
                    setattr(self, 'width', args[j])
                    setattr(self, 'height', args[j])
                else:
                    setattr(self, list_str[j], args[j])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns attributes """
        list_str = ['id', 'size', 'x', 'y']
        dict_atr = {}

        for key in list_atr:
            if key == 'size':
                dict_atr[key] = getattr(self, 'width')
            else:
                dict_atr[key] = getattr(self, key)

        return dict_atr

    def to_dictionary(self):
        """Return the dictionary of the  Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
