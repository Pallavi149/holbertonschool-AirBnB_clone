#!/usr/bin/python3
"""Test for State Class"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Class of State"""

    def test_init(self):
        s = State()
        self.assertIsInstance(s, State)

    def test_name(self):
        s = State()
        self.assertEqual(s.name, "")

    def test_name_setter(self):
        s = State()
        s.name = "Cranny"
        self.assertEqual(s.name, "Cranny")


