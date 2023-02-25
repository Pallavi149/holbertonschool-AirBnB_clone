#!/usr/bin/python3
"""Test Cases for Base Model Class"""
import time
import unittest
from datetime import datetime
from models.base_model import BaseModel
from time import sleep

class TestBaseModel(unittest.TestCase):
    """Test Cases for Base Model"""

    def test_save_method_updates_updated_at_attribute(self):
        """
        Tests that calling the save() method updates the 'updated_at' attribute
        with a new datetime object.
        """
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        new_updated_at = model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertIsInstance(new_updated_at, datetime)
        self.assertLess(old_updated_at, new_updated_at)

    def test_save_can_update_updated_at_multiple_times(self):
        """
        Tests that calling the save() method multiple times updates the 'updated_at'
        attribute with a new datetime object each time.
        """
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        new_updated_at = model.updated_at
        self.assertLess(old_updated_at, new_updated_at)
        sleep(0.01)
        model.save()
        newer_updated_at = model.updated_at
        self.assertLess(new_updated_at, newer_updated_at)
        self.assertIsInstance(newer_updated_at, datetime)

    def test_save_updates_json_file(self):
        """
        Tests that calling the save() method updates the JSON file with a new entry
        for the instance of the BaseModel class.
        """
        model = BaseModel()
        model.save()
        model_id = "BaseModel.{}".format(model.id)
        with open("file.json", "r", encoding="utf-8") as f:
            file_data = f.read()
        self.assertIn(model_id, file_data)

    def test_to_dict(self):
        """Test to_dict returns a dictionary with all instance attributes"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_id(self):
        """Check if id is a string and unique for each instance"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertIsInstance(model1.id, str)
        self.assertIsInstance(model2.id, str)
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at(self):
        """
        Test that created_at attribute is a datetime object and is set
        to the current datetime when an instance is created
        """
        model = BaseModel()
        time.sleep(0.00001)
        created_at_timestamp = model.created_at.timestamp()
        updated_at_timestamp = model.updated_at.timestamp()
        self.assertIsInstance(model.created_at, datetime)
        self.assertAlmostEqual(
                created_at_timestamp,
                updated_at_timestamp,
                places=1)

    def test_str(self):
        """Test __str__ return string format"""
        model = BaseModel()
        model_str = str(model)
        self.assertIn('[BaseModel]', model_str)
        self.assertIn(model.id, model_str)
        self.assertIn(str(model.__dict__), model_str)
