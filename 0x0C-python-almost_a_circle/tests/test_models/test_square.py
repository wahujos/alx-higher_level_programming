#!/usr/bin/python3
"""handle module imports"""
from models.rectangle import Rectangle
from models.square import Square
import unittest


class TestSquare(unittest.TestCase):
    """defining the class that will hold the tests for the square"""
    def test_size_getter(self):
        '''testing getter for the size'''
        sqr = Square(5)
        self.assertEqual(sqr.size, 5)

    def test_size_setter(self):
        '''testing setter for the size'''
        sqr = Square(5)
        sqr.size = 10
        self.assertEqual(sqr.size, 10)
        self.assertEqual(sqr.width, 10)
        self.assertEqual(sqr.height, 10)

        with self.assertRaises(ValueError):
            sqr.size = -4




if __name__ == '__main__':
    unittest.main()
