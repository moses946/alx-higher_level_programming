""" test class for base class
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ Unit tests for base class"""
    def setUp(self):
        self.base = Base()

    def test_from_json_string(self):
        s = [{'id': 1}]
        self.assertEqual(self.base.from_json_string('[{"id": 1}]'), s)
        self.assertEqual(self.base.from_json_string('[]'), [])
        self.assertEqual(self.base.from_json_string(None), [])


if __name__ == '__main__':
    unittest.main()
