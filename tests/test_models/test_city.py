#!/usr/bin/python3
"""Test for City Class"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Class of Amenity"""

    def test_init(self):
        """Check initialise city"""
        c = City()
        self.assertIsInstance(c, City)

    def test_state_id(self):
        """Check city id"""
        c = City()
        self.assertEqual(c.state_id, "")

    def test_name(self):
        """Check city name"""
        c = City()
        self.assertEqual(c.name, "")

    def test_name_setter(self):
        """Set city name"""
        c = City()
        c.name = "Clayton South"
        self.assertEqual(c.name, "Clayton South")

