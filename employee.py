class Employee:
    """Base class for all Employees"""

    dictionary = {'_emp_id': 'emp_id', '_gender':'gender',
                  '_age': 'age', '_sales': 'sales',
                  '_bmi': 'bmi', '_salary': 'salary',
                  '_birthday': 'birthday'}

    def __init__(self, dictionary):
        self.__dict__.update(dictionary)

    def get_all_data(self):
        employee_info = [self._emp_id, self._gender, self._age, self._sales, self._bmi, self._salary, self._birthday]
        return employee_info

