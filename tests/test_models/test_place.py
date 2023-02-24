#!/usr/bin/python3
"""Test for Place Class"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Class of place"""

    def test_init(self):
        """Check initialise amenity"""
        p = Place()
        self.assertIsInstance(p, Place)

    def test_city_id(self):
        """Test city id"""
        p = Place()
        self.assertEqual(p.city_id, "")

    def test_user_id(self):
        """Test user id"""
        p = Place()
        self.assertEqual(p.user_id, "")

    def test_name(self):
        """Test place name"""
        p = Place()
        self.assertEqual(p.name, "")

    def test_description(self):
        """Test desription"""
        p = Place()
        self.assertEqual(p.description, "")

    def test_number_rooms(self):
        """Test number of rooms"""
        p = Place()
        self.assertEqual(p.number_rooms, 0)

    def test_number_bathrooms(self):
        """Test number of bathrooms"""
        p = Place()
        self.assertEqual(p.number_bathrooms, 0)

    def test_max_guest(self):
        """Test number of bathrooms"""
        p = Place()
        self.assertEqual(p.max_guest, 0)

    def test_price_by_night(self):
        """Test number of bathrooms"""
        p = Place()
        self.assertEqual(p.price_by_night, 0)

    def test_latitude(self):
        """test latitude"""
        p = Place()
        self.assertEqual(p.latitude, 0.0)

    def test_longitude(self):
        """test longitude"""
        p = Place()
        self.assertEqual(p.longitude, 0.0)

    def test_amenity_ids(self):
        """test amenity ids"""
        p = Place()
        self.assertEqual(p.amenity_ids, [])

    def test_amenity_ids_setter(self):
        """Test amenity id setter"""
        p = Place()
        p.amenity_ids = ["wifi", "pool"]
        self.assertEqual(p.amenity_ids, ["wifi", "pool"])
