#!/usr/bin/python3
"""test case"""
import unittest
import calc


class TestClass(unittest.TestCase):
    """a class that inherits from unittest"""

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, -1), -2)
        self.assertEqual(calc.add(-1, 1), 0)

    def test_devide(self):
        self.assertEqual(calc.devide(10, 5), 2)
        self.assertEqual(calc.devide(1, -1), -1)
        self.assertEqual(calc.devide(-1, -1), 1)

        self.assertRaises(ValueError, calc.devide, 10, 0)


if "__name__" == "__main__":
    unittest.main()
