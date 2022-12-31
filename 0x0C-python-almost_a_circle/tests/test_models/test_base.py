#!/usr/bin/python3
"""
module contains tetscase for class base
"""


import unittest


from models.base import Base


class TestBase(unittest.TestCase):
    def test_id(self):
        Base._Base__nb_objects = 0
        b = Base()
        b1 = Base()
        b2 = Base()
        self.assertIsNotNone(b.id)
        self.assertGreater(b.id, 0)
