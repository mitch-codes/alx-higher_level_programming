#!/usr/bin/python3
"""test base class"""
import sys
sys.path.append("..")
import unittest
from models.base import Base


class BaseTest(unittest.TestCase):
    """create a clase"""

    def test_base(self):
        myBase = Base(22)
        print(myBase.id)
