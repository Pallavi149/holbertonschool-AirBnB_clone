#!/usr/bin/python3
"""Test for Review Class"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Class of Review"""

    def test_init(self):
        """Check initialise review"""
        r = Review()
        self.assertIsInstance(r, Review)

    def test_place_id(self):
        """Test Place id"""
        r = Review()
        self.assertEqual(r.place_id, "")

    def test_user_id(self):
        """Test user id"""
        r = Review()
        self.assertEqual(r.user_id, "")

    def test_text(self):
        """Test text"""
        r = Review()
        self.assertEqual(r.text, "")

    def test_text_setter(self):
        """Test text setter"""
        r = Review()
        r.text = "Great place to stay!"
        self.assertEqual(r.text, "Great place to stay!")

