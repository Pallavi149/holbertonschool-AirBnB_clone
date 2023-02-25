#!/usr/bin/python3
"""TestFileStorage class"""

import os
import json
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Class for TestFileStorage"""

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        "Remove the test file if it was created during testing"
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_file_path(self):
        "Test that the file path is correct"
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects(self):
        "Test that the objects dictionary is created"
        self.assertEqual(type(self.storage._FileStorage__objects), dict)

    def test_all(self):
        "Test that the all() method returns the correct dictionary of objects"
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.assertNotEqual(self.storage.all(), {})

    def test_new(self):
        "Test that new() adds an object to the dictionary of objects"
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        key = model.id
        self.assertFalse(key in self.storage.all())

    def test_save(self):
        "Test that save() writes the dictionary of objects to the JSON file"
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))
        with open(self.storage._FileStorage__file_path, 'r') as f:
            data = json.load(f)
        self.assertTrue(model.to_dict() in data.values())

    def test_reload(self):
        "Test that reload() loads the dictionary of objects from the JSON file"
        model = BaseModel()
        obj = BaseModel()
        obj.save()
        with open(self.storage._FileStorage__file_path, "r") as f:
            saved_data = json.load(f)
        self.assertIn("BaseModel.{}".format(obj.id), saved_data)
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        self.assertIn("BaseModel.{}".format(obj.id), self.storage.all())
        loaded_obj = self.storage.all()["BaseModel.{}".format(obj.id)]
        self.assertIsInstance(loaded_obj, BaseModel)
        self.assertEqual(loaded_obj.id, obj.id)
