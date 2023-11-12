#!/usr/bin/python3
"""Module Rectangle class"""

from models.base import Base

class Rectangle(Base):
    """class rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize  Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get height."""
        return self.__height

    @height.setter
    def height(self, value):
        """set height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter  x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter x."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter y."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area Rectangle."""
        return self.__width * self.__height

    def display(self):
        """ displays a rectangle """
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"

        print(rectangle, end='')

    def __str__(self):
        """ str method """
        str_rectangle = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_rectangle + str_id + str_xy + str_wh
    
    def update(self, *args, **kwargs):
        """ update method """
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for j in range(len(args)):
                setattr(self, list_atr[j], args[j])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
       
     def to_dictionary(self):
        """Return a Rectangle."""
        dictionary = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        
        return dictionary
    








