"""Tests for .csv phone book app"""

import csv
import os
import unittest

from actions.crud import create, update, delete
from utils.csv_data import fields


class TestCRUD(unittest.TestCase):
    """.csv CRUD testing case"""

    path = "../tests/test.csv"

    def test_csv(self):
        """Testing create .csv func"""

        create(p=self.path)
        self.assertEqual(True, os.path.exists(self.path))
        os.remove(self.path)

    def test_csv_headers(self):
        """Testing .csv headers schema"""

        create(p=self.path)
        with open(self.path, "rt", encoding="utf-8") as f:
            reader = csv.reader(f)
            headers = next(reader)
            for field in fields:
                headers.remove(field)
            self.assertEqual(0, len(headers))
            os.remove(self.path)

    def test_csv_create(self):
        """Testing adding new record"""

        create(p=self.path)
        fds = [
            "Paul",
            "Smith",
            "Batkovich",
            "COMPANY",
            "+1 (123) 456 7890",
            "+2 (123) 456 7890",
        ]
        create(data=fds, p=self.path)
        with open(self.path, "rt", encoding="utf-8") as f:
            reader = csv.reader(f)
            _ = next(reader)
            new_record = next(reader)
            for field in fds:
                new_record.remove(field)
            self.assertEqual(0, len(new_record))
            os.remove(self.path)

    def test_csv_update(self):
        """Testing update record"""

        create(p=self.path)
        fds = [
            "Paul",
            "Smith",
            "Batkovich",
            "COMPANY",
            "+1 (123) 456 7890",
            "+2 (123) 456 7890",
        ]
        create(data=fds, p=self.path)
        updated = [
            "Paul",
            "Smith",
            "Batkovich",
            "EFFECTIVE",
            "+1 (123) 456 7890",
            "+2 (123) 456 7890",
        ]
        update_data = {"0": ("company", "EFFECTIVE")}
        update(update_data=update_data, p=self.path)
        with open(self.path, "rt", encoding="utf-8") as f:
            reader = csv.reader(f)
            _ = next(reader)
            updated_record = next(reader)
            for field in updated:
                updated_record.remove(field)
            self.assertEqual(0, len(updated_record))
            os.remove(self.path)

    def test_csv_delete(self):
        """Testing delete record"""

        create(p=self.path)
        fds = [
            "Paul",
            "Smith",
            "Batkovich",
            "COMPANY",
            "+1 (123) 456 7890",
            "+2 (123) 456 7890",
        ]
        create(data=fds, p=self.path)
        delete(row=0, p=self.path)
        with open(self.path, "rt", encoding="utf-8") as f:
            reader = csv.reader(f)
            _ = next(reader)
            try:
                next(reader)
            except StopIteration:
                pass
            os.remove(self.path)


if __name__ == "__main__":
    unittest.main()
