import unittest
from employee_database import EmployeeDatabase
from controller import Controller
import os


class DatabaseUnitTest(unittest.TestCase):
    def test_database_created(self):
        c = Controller()
        c.db.create_connection("test_case.db")
        result = os.path.isfile("test_case.db")
        self.assertTrue(result)

    def test_database_employee_table_created(self):
        c = Controller()
        content = [("A001", "M", 26, 200, "Normal", 20, "08-10-1991"),
                   ("A002", "F", 26, 300, "Normal", 30, "09-10-1991")]
        c.add_to_database(content)
        database = c.get_all_employees()
        self.assertEqual(database, content)