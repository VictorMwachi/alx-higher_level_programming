#!/usr/bin/python3
"""
module contains tetscase for class base
"""


import unittest


from models.base import Base


class TestBase(unittest.TestCase):
    def test_init(self):
        b = Base()
        self.assertIsNotNone(b)
