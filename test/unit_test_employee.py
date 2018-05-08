import unittest
from employee import Employee


class EmployeeUnitTest(unittest.TestCase):

    def test_employee_id(self):
        dictionary = {'_emp_id': 'A001', '_gender': 'M', '_age': '26',
                      '_sales': '200','_bmi': 'Normal',
                      '_salary': '20', '_birthday': '08-10-1991'}
        e = Employee(dictionary)
        expected = 'A001'
        self.assertEqual(expected, e._emp_id)

    def test_employee_gender(self):
        dictionary = {'_emp_id': 'A001', '_gender': 'M', '_age': '26',
                      '_sales': '200','_bmi': 'Normal',
                      '_salary': '20', '_birthday': '08-10-1991'}
        e = Employee(dictionary)
        expected = 'M'
        self.assertEqual(expected, e._gender)

    def test_employee_age(self):
        dictionary = {'_emp_id': 'A001', '_gender': 'M', '_age': '26',
                      '_sales': '200','_bmi': 'Normal',
                      '_salary': '20', '_birthday': '08-10-1991'}
        e = Employee(dictionary)
        expected = '26'
        self.assertEqual(expected, e._age)

    def test_get_all_data(self):
        dictionary = {'_emp_id': 'A001', '_gender': 'M', '_age': '26',
                      '_sales': '200','_bmi': 'Normal',
                      '_salary': '20', '_birthday': '08-10-1991'}
        e = Employee(dictionary)
        expected = ['A001', 'M', '26', '200', 'Normal', '20', '08-10-1991']
        actual = e.get_all_data()
        self.assertEqual(expected, actual)

    def test_get_all_data_notEqual(self):
        dictionary = {'_emp_id': 'A001', '_gender': 'M', '_age': '26',
                      '_sales': '200','_bmi': 'Normal',
                      '_salary': '20', '_birthday': '08-10-1991'}
        e = Employee(dictionary)
        expected = ['A001', 'M', '200', 'Normal', '20', '08-10-1991']
        actual = e.get_all_data()
        self.assertNotEqual(expected, actual)
