import unittest
from controller import Controller


class ControllerUnitTest(unittest.TestCase):
    def test_validate_items_returns_valid(self):
        """
        test if items return validated
        """
        c = Controller()
        content = [("A001", "M", 26, 200, "Normal", 20, "08-10-1991"),
                   ("A002", "F", 26, 300, "Normal", 30, "09-10-1991")]
        validated = c.validate_items(content)
        valid = len(validated['Valid'])
        expected = 2
        self.assertEqual(valid, expected, "incorrect validator")

    def test_validate_items_returns_invalid(self):
        """
        test if invalid items also return
        """
        c = Controller()
        content = [("A001", "M", 26, 200, "Normal", 20, "08-10-1991"),
                   ("A002", "F", 26, 300, "Normal", 30, "09-10-1991"),
                   ("A003", "Female", 44, "", "Fat", 90, "")]
        validated = c.validate_items(content)
        valid = len(validated['Invalid'])
        expected = 1
        self.assertEqual(valid, expected, "incorrect validator")

    def test_validate_items_returns_both_valid_and_invalid(self):
        """
        test is both valid and invalid return in dict
        """
        c = Controller()
        content = [("A001", "M", 26, 200, "Normal", 20, "08-10-1991"),
                   ("A002", "F", 26, 300, "Normal", 30, "09-10-1991"),
                   ("A003", "Female", 44, "", "Fat", 90, "")]
        validated = c.validate_items(content)
        valid = len(validated['Invalid'])
        expected = 1
        self.assertEqual(valid, expected, "incorrect validator")

    def test_add_to_database_adds_employees(self):
        """
        test if employees can be added to db
        """
        c = Controller()
        content = [("A001", "M", 26, 200, "Normal", 20, "08-10-1991"),
                   ("A002", "F", 26, 300, "Normal", 30, "09-10-1991")]
        c.add_to_database(content)
        database = c.get_all_employees()
        self.assertEqual(database, content)

    def test_get_all_employees_returns_employees(self):
        c = Controller()
        content = [("A001", "M", 26, 200, "Normal", 20, "08-10-1991"),
                   ("A002", "F", 26, 300, "Normal", 30, "09-10-1991")]
        c.add_to_database(content)
        database = c.get_all_employees()
        self.assertEqual(database, content)

    def test_get_all_employees_returns_none_when_database_created(self):
        c = Controller()
        c.db.create_connection("test2.db")
        database = c.get_all_employees()
        self.assertEqual(database, None)

    def test_load_file_name_error(self):
        """
        test is extension file name wrong
        """
        c = Controller()
        fun = c.load_file("test.xx")
        self.assertRaises(NameError, fun)

    def test_load_file_no_found_error(self):
        """
        test if file not found
        """
        c = Controller()
        fun = c.load_file("test999999999999.csv")
        self.assertRaises(FileNotFoundError, fun)

    def test_load_file_exception(self):
        """
        test file name no extension
        """
        c = Controller()
        fun = c.load_file("test999999999999")
        self.assertRaises(Exception, fun)

