import csv
import os
import unittest

from actions.crud import create
from utils.csv_data import fields


class TestPhoneBook(unittest.TestCase):
    path = "../tests/test.csv"

    def setUp(self):
        create(p=self.path)

    def tearDown(self):
        os.remove(self.path)

    def test_csv_create(self):
        self.assertEqual(True, os.path.exists(self.path))

    def test_csv_headers(self):
        with open(self.path, "rt") as f:
            reader = csv.reader(f)
            headers = next(reader)
            for field in fields:
                headers.remove(field)
            self.assertEqual(0, len(headers))


if __name__ == "__main__":
    unittest.main()
