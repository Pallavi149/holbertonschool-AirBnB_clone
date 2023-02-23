#!/usr/bin/python3
"""Test cases for user"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for user"""

    def test_email(self):
        """Test that the default value of email is an empty string"""
        user = User()
        self.assertEqual(user.email, "")
        user.email = "yoza@yoza.uso"
        self.assertEqual(user.email, "yoza@yoza.uso")

    def test_password(self):
        """Test that the default value of password is an empty string"""
        user = User()
        self.assertEqual(user.password, "")
        user.password = "ilovechickenwings"
        self.assertEqual(user.password, "ilovechickenwings")

    def test_first_name(self):
        """Test that the default value of first_name is an empty string"""
        user = User()
        self.assertEqual(user.first_name, "")
        user.first_name = "Pallavi"
        self.assertEqual(user.first_name, "Pallavi")

    def test_last_name(self):
        """Test that the default value of last_name is an empty string"""
        user = User()
        self.assertEqual(user.last_name, "")
        user.last_name = "Eps"
        self.assertEqual(user.last_name, "Eps")
