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
        b3 =Base(89)
        self.assertEqual(b.id, 1)
        self.assertEqual(b1.id, 2)
        self.assertEqual(b2.id, 3)
        self.assertEqual(b3.id, 89)
        self.assertGreater(b.id, 0)
