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
        self.storage - FileStorage()

    def tearDown(self):
        if os.path.exists(self.storage._FileStorage__file_path):
            os.remove(self.storage._FileStorage__file_path)

    def test_file_path(self):
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_objects(self):
        self.assertEqual(type(self.storage._FileStorage__objects), dict)

    def test_all(self):
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        model = BaseModel()
        self.storage.new(model)
        key = f"{model.__class__.__name__},{model.id}"
        self.assertTrue(key in self.storage.all())

    def test_save(self):
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))
        with open(self.storage._FileStorage__file_path, 'r') as f:
            data = json.load(f)
        key = f"{model.__class__.__name__},{model.id}"
        self.assertTrue(key in data)

    def test_reload(self):
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage.reload()
        key = f"{model.__class__.__name__},{model.id}"
        self.assertTrue(key in self.storage.all())
