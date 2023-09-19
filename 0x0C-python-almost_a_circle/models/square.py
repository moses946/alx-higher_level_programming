""" module containing square class
"""


from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """ inherits from rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize Square class"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return f"[Square] ({self.id} {self.x}/{self.y} - {self.size})"

    @property
    def size(self):
        """size getter method"""
        return self.width

    @size.setter
    def size(self, value):
        """ size setter method"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Updates the attributes"""
        attributes = ["id", "width", "height", "x", "y"]
        if args and len(args) > 0:
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)
        else:
            for attribute, value in kwargs.items():
                setattr(self, attribute, value)

    def to_dictionary(self):
        """ Return dictionary representation of class instance"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y,
        }
