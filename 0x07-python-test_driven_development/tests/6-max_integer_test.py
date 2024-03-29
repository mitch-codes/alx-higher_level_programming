#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMax(unittest.TestCase):
    
    def test_max_func(self):
        self.assertEqual(max_integer([3, 1, 2]), 3)
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([1, 2, -3]), 2)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertRaises(TypeError, max_integer, [1, 2, "a"])
