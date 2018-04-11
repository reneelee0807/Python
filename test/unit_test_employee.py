import unittest
from employee import Employee


class EmployeeUnitTest(unittest.TestCase):

    def test_employee_id(self):
        e = Employee('A001', 'M', '26', '200', 'Normal', '20', '08-10-1991')
        expected = 'A001'
        self.assertEqual(expected, e._emp_id)


    def test_employee_gender(self):
        e = Employee('A001', 'M', '26', '200', 'Normal', '20', '08-10-1991')
        expected = 'M'
        self.assertEqual(expected, e._gender)


    def test_employee_age(self):
        e = Employee('A001', 'M', '26', '200', 'Normal', '20', '08-10-1991')
        expected = '26'
        self.assertEqual(expected, e._age)
