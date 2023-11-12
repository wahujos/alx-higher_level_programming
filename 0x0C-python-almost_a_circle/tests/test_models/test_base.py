#!/usr/bin/python3
"""handling documentation"""


import unittest
from models.base import Base
"""Handle the various other files that we will use"""


class TestBase(unittest.TestCase):
    """This is where we have our test and this inherits from the Unit test"""
    def test_initialize(self):
        """This test checks whether the function is initialized anytime we create an object or an instance of a class"""
        base = Base()
        self.assertEqual(base.id, 1)

    def test_with_specific_number(self):
        "This test whether initialization takes place with a specific number of the id"""
        base = Base(id=3)
        self.assertEqual(base.id, 3)

    def test_with_different_instances(self):
        "This test whether the function works with different instances"""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 2)
        self.assertEqual(base2.id, 3)


if __name__ == '__main__':
    unittest.main()
