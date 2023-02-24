#!/usr/bin/python3
"""Test for Amenity Class"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Class of Amenity"""

    def test_init(self):
        """Check initialise amenity"""
        a = Amenity()
        self.assertIsInstance(a, Amenity)

    def test_name(self):
        """Check Amenity name"""
        a = Amenity()
        self.assertEqual(a.name, "")

    def test_name_setter(self):
        """Set Amenity name is set correctly"""
        a = Amenity()
        a.name = "Pool"
        self.assertEqual(a.name, "Pool")


