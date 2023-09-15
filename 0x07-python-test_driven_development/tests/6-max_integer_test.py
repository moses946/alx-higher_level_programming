#!/usr/bin/python3
""" Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Tests for all edge cases for the function ``max_integer``
    """
    def test_max_int(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 4, 5]), 5)
        self.assertEqual(max_integer([5, 4, 1]), 5)
        self.assertEqual(max_integer([4, 5, 1]), 5)
        self.assertEqual(max_integer([4, 5, -1]), 5)
        self.assertEqual(max_integer([-4, -5, -1]), -1)
        self.assertEqual(max_integer([5]), 5)


        with self.assertRaises(TypeError):
            max_integer([1, 4, "Hello"])
            max_integer(["Hello", "Hi", "Like"])


if __name__ == "__main__":
    unittest.main()
