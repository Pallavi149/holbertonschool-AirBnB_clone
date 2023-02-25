#!/usr/bin/python3
"""Test Cases for Base Model Class"""
import unittest
import time
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test Cases for Base Model"""

    def test_save(self):
        "Test that save updates update_at with the current datetime"
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

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
        start_time = datetime.now()
        model = BaseModel()
        end_time = datetime.now()
        self.assertTrue(start_time <= model.created_at <= end_time)
        time.sleep(1e-4)
        start_time = datetime.now()
        inst2 = BaseModel()
        end_time = datetime.now()
        self.assertTrue(start_time <= inst2.created_at <= end_time)
        self.assertEqual(model.created_at, model.updated_at)
        self.assertEqual(inst2.created_at, inst2.updated_at)
        self.assertNotEqual(model.created_at, inst2.created_at)
        self.assertNotEqual(model.updated_at, inst2.updated_at)

    def test_str(self):
        """Test __str__ return string format"""
        model = BaseModel()
        model_str = str(model)
        self.assertIn('[BaseModel]', model_str)
        self.assertIn(model.id, model_str)
        self.assertIn(str(model.__dict__), model_str)
