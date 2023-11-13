#!/usr/bin/python3
"""handle module documentations"""
import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys
"""handling various files needed fot the tests"""


class Test_Rectangele(unittest.TestCase):
    """defining the class that inherits from the unittest"""
    def test_initialization(self):
        """ testing initialization of the function"""
        rect1 = Rectangle(10, 20, 5, 6, 1)
        self.assertEqual(rect1.width, 10)
        self.assertEqual(rect1.height, 20)
        self.assertEqual(rect1.x, 5)
        self.assertEqual(rect1.y, 6)
        self.assertEqual(rect1.id, 1)

    def test_width_property(self):
        """testing the width property"""
        rect1 = Rectangle(10, 20, 5, 6, 1)
        rect1.width = 12
        self.assertEqual(rect1.width, 12)

    def test_height_property(self):
        rect1 = Rectangle(10, 20, 5, 6, 1)
        rect1.height = 22
        self.assertEqual(rect1.height, 22)

    def test_x_property(self):
        rect1 = Rectangle(10, 20, 5, 6, 1)
        rect1.x = 8
        self.assertEqual(rect1.x, 8)

    def test_y_property(self):
        rect1 = Rectangle(10, 20, 5, 6, 1)
        rect1.y = 15
        self.assertEqual(rect1.y, 15)

    def test_invalid_width(self):
        with self.assertRaises(TypeError):
            rect1 = Rectangle("10", 20, 5, 6, 1)

        with self.assertRaises(TypeError):
            rect1 = Rectangle([10], 20, 5, 6, 1)

        with self.assertRaises(TypeError):
            rect1 = Rectangle({10}, 20, 5, 6, 1)

        with self.assertRaises(TypeError):
            rect1 = Rectangle((10, ), 20, 5, 6, 1)

        with self.assertRaises(ValueError):
            rect1 = Rectangle(-1, 20, 5, 6, 1)

        with self.assertRaises(ValueError):
            rect1 = Rectangle(0, 20, 5, 6, 1)

    def test_invalid_height(self):
        with self.assertRaises(TypeError):
            rect1 = Rectangle(10, "20", 5, 6, 1)

        with self.assertRaises(TypeError):
            rect1 = Rectangle(10, [20], 5, 6, 1)

        with self.assertRaises(TypeError):
            rect1 = Rectangle(10, {20}, 5, 6, 1)

        with self.assertRaises(TypeError):
            rect1 = Rectangle(10, (20, ), 5, 6, 1)

        with self.assertRaises(ValueError):
            rect1 = Rectangle(10, -20, 5, 6, 1)

        with self.assertRaises(ValueError):
            rect1 = Rectangle(10, 0, 5, 6, 1)

    def test_invalid_x(self):
        with self.assertRaises(TypeError):
            rect1 = Rectangle(10, 20, "5", 6, 1)

        with self.assertRaises(TypeError):
            rect1 = Rectangle(10, 20, [5], 6, 1)

        with self.assertRaises(TypeError):
            rect1 = Rectangle(10, 20, {5}, 6, 1)

        with self.assertRaises(TypeError):
            rect1 = Rectangle(10, 20, (5, ), 6, 1)

        with self.assertRaises(ValueError):
            rect1 = Rectangle(10, 20, -5, 6, 1)

    def test_invalid_y(self):
        with self.assertRaises(TypeError):
            rect1 = Rectangle(10, 20, 5, "6", 1)

        with self.assertRaises(TypeError):
            rect1 = Rectangle(10, 20, 5, [6], 1)

        with self.assertRaises(TypeError):
            rect1 = Rectangle(10, 20, 5, {6}, 1)

        with self.assertRaises(TypeError):
            rect1 = Rectangle(10, 20, 5, (6, ), 1)

        with self.assertRaises(ValueError):
            rect1 = Rectangle(10, 20, 5, -6, 1)

    def test_area_instance(self):
        rect1 = Rectangle(10, 20)
        self.assertEqual(rect1.area(), 200)

        rect1.width = 15
        rect1.height = 25
        self.assertEqual(rect1.area(), 375)

        rect2 = Rectangle(10000, 100000)
        self.assertEqual(rect2.area(), 1000000000)

    def setUp(self):
        """self.saved_stdout = sys.stdout
        sys.stdout = StringIO()"""
        self.saved_output = StringIO()
        self.actual_output = StringIO()

    def tearDown(self):
        """sys.stdout = self.saved_stdout"""
        self.saved_output.close()
        self.actual_output.close()

    def test_display_rectangle_output_with_offset(self):
        """test a rectangle with the offset"""
        rect2 = Rectangle(2, 3, 2, 2)
        sys.stdout = self.actual_output
        rect2.display()
        sys.stdout = sys.__stdout__
        actual_output = self.actual_output.getvalue()
        self.assertEqual(actual_output, '\n\n  ##\n  ##\n  ##\n')

    def test_display_rectangle_output_without_offset(self):
        """test a rectangle with out the offset"""
        sys.stdout = self.actual_output
        rect1 = Rectangle(3, 4)
        rect1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(self.actual_output.getvalue(), '###\n###\n###\n###\n')

    def test__str__(self):
        """test the str function"""
        rect1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(rect1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

        rect2 = Rectangle(5, 5, 1, 0, 4)
        self.assertEqual(rect2.__str__(), "[Rectangle] (4) 1/0 - 5/5")

    def test_update_args(self):
        """test the args function"""
        rect1 = Rectangle(3, 4, 1, 2, 5)
        rect1.update(10, 15, 20, 25, 35)

        self.assertEqual(rect1.id, 10)
        self.assertEqual(rect1.width, 15)
        self.assertEqual(rect1.height, 20)
        self.assertEqual(rect1.x, 25)
        self.assertEqual(rect1.y, 35)

        rect2 = Rectangle(1, 2, 3, 4, 5)
        rect2.update(5, 10, 20, 3, 4)

        self.assertEqual(rect2.id, 5)
        self.assertEqual(rect2.width, 10)
        self.assertEqual(rect2.height, 20)
        self.assertEqual(rect2.x, 3)
        self.assertEqual(rect2.y, 4)

        rect3 = Rectangle(1, 2, 3, 4, 5)
        rect3.update()

        self.assertEqual(rect3.id, 5)
        self.assertEqual(rect3.width, 1)
        self.assertEqual(rect3.height, 2)
        self.assertEqual(rect3.x, 3)
        self.assertEqual(rect3.y, 4)
        rect4 = Rectangle(3, 4, 5, 6, 7)
        with self.assertRaises(TypeError):
            rect4.update(10, "invalid", 30, 35, 40)

        with self.assertRaises(ValueError):
            rect4.update(10, -1, 30, 35, 40)

        with self.assertRaises(TypeError):
            rect4.update(10, {20}, 30, 35, 40)

    def test_update_kwags(self):
        rect1 = Rectangle(1, 2, 3, 4, 5)
        rect1.update(id=10, width=15, height=20, x=2, y=3)
        self.assertEqual(rect1.id, 10)
        self.assertEqual(rect1.width, 15)
        self.assertEqual(rect1.height, 20)
        self.assertEqual(rect1.x, 2)
        self.assertEqual(rect1.y, 3)

        rect2 = Rectangle(1, 2, 3, 4, 5)
        rect2.update(width=10, x=4, y=5, id=8, height=20)
        self.assertEqual(rect2.id, 8)
        self.assertEqual(rect2.width, 10)
        self.assertEqual(rect2.height, 20)
        self.assertEqual(rect2.x, 4)
        self.assertEqual(rect2.y, 5)

    if __name__ == '__main__':
        unittest.main()
