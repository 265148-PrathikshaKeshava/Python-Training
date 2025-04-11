import unittest
from storage import Storage
import os
import json

class TestStorage(unittest.TestCase):

    def setUp(self):
        self.storage = Storage(filepath="test_students.json")
        self.test_data = [
            {"id": "1", "name": "Anil", "age": 12, "grade": "6"},
            {"id": "2", "name": "Sita", "age": 14, "grade": "8"}
        ]
        # Clean up before starting tests
        if os.path.exists(self.storage.filepath):
            os.remove(self.storage.filepath)

    def test_save_and_load(self):
        # Save data
        self.storage.save(self.test_data)

        # Load data
        loaded_data = self.storage.load()
        self.assertEqual(loaded_data, self.test_data)

    def test_load_empty_file(self):
        # Simulate an empty file
        if os.path.exists(self.storage.filepath):
            os.remove(self.storage.filepath)

        # Load from the empty file
        loaded_data = self.storage.load()
        self.assertEqual(loaded_data, [])

    def test_save_invalid_data(self):
        invalid_data = {"id": "3", "name": "Ravi"}  # Missing age and grade
        with self.assertRaises(TypeError):
            self.storage.save(invalid_data)
