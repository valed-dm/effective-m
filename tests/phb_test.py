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

    def test_csv(self):
        self.assertEqual(True, os.path.exists(self.path))

    def test_csv_headers(self):
        with open(self.path, "rt") as f:
            reader = csv.reader(f)
            headers = next(reader)
            for field in fields:
                headers.remove(field)
            self.assertEqual(0, len(headers))

    def test_csv_create(self):
        fds = [
            "Paul",
            "Smith",
            "Batkovich",
            "COMPANY",
            "+1 (123) 456 7890",
            "+2 (123) 456 7890",
        ]
        create(data=fds, p=self.path)
        with open(self.path, "rt") as f:
            reader = csv.reader(f)
            _ = next(reader)
            new_record = next(reader)
            for field in fds:
                new_record.remove(field)
            self.assertEqual(0, len(new_record))


if __name__ == "__main__":
    unittest.main()
