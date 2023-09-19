""" test class for base class
"""


import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rect = Rectangle(1, 2, 0, 0, 2)

    def test_width(self):
        self.assertEqual(self.rect.width, 1)
        with self.assertRaises(TypeError):
            self.rect.width = "invalid"
        with self.assertRaises(ValueError):
            self.rect.width = 0

    def test_height(self):
        self.assertEqual(self.rect.height, 2)
        with self.assertRaises(TypeError):
            self.rect.height = "invalid"
        with self.assertRaises(ValueError):
            self.rect.height = 0

    def test_x(self):
        self.assertEqual(self.rect.x, 0)
        with self.assertRaises(TypeError):
            self.rect.x = "invalid"
        with self.assertRaises(ValueError):
            self.rect.x = -1

    def test_y(self):
        self.assertEqual(self.rect.y, 0)
        with self.assertRaises(TypeError):
            self.rect.y = "invalid"
        with self.assertRaises(ValueError):
            self.rect.y = -1

    def test_area(self):
        self.assertEqual(self.rect.area(), 2)

    def test_update(self):
        self.rect.update(width=3, height=4)
        self.assertEqual(self.rect.width, 3)
        self.assertEqual(self.rect.height, 4)

    def test_to_dictionary(self):
        dict_ = self.rect.to_dictionary()
        expected_dict = {'width': 1, 'height': 2, 'x': 0, 'y': 0, 'id': 2}
        self.assertDictEqual(dict_, expected_dict)

if __name__ == '__main__':
    unittest.main()
