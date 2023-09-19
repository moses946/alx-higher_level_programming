""" test class for base class
"""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def setUp(self):
        self.square = Square(1)

    def test_size(self):
        self.assertEqual(self.square.size, 1)
        with self.assertRaises(TypeError):
            self.square.size = "invalid"
        with self.assertRaises(ValueError):
            self.square.size = 0

    def test_update(self):
        self.square.update(size=2)
        self.assertEqual(self.square.size, 2)

    def test_to_dictionary(self):
        dict_ = self.square.to_dictionary()
        expected_dict = {'id': 1, 'size': 1, 'x': 0, 'y': 0}
        self.assertDictEqual(dict_, expected_dict)

if __name__ == '__main__':
    unittest.main()
