#!/usr/bin/python3
""" module containing rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """ Rectangle class inheriting from Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize Rectangle class
        Args:
            width (int): Integer
            height (int): Integer
            x (int): Integer
            y (int): Integer
            id: Unique identifier
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ width getter method """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter method """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter method"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x getter method """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter method"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter method """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter method"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return area of rectangle instance"""
        return self.__height * self.__width

    def display(self):
        """Prints the rectangle with character '#' """
        for i in range(self.__y):
            print()
        for row in range(self.__width):
            for i in range(self.__x):
                print(" ", end="")
            for column in range(self.__height):
                print('#', end="")
            print()

    def __str__(self):
        h = self.__height
        w = self.__width
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {w}/{h}"

    def update(self, *args, **kwargs):
        """ Updates the attributes"""
        attributes = ["id", "width", "height", "x", "y"]
        if args and len(args) > 0:
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)
        else:
            for attribute, value in kwargs.items():
                if hasattr(self, attribute):
                    setattr(self, attribute, value)

    def to_dictionary(self):
        """ Return dict representation of class instance"""
        return {
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y,
            'id': self.id,
        }
