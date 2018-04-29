class Employee:
    """Base class for all Employees"""

    dictionary = {'_emp_id': 'emp_id', '_gender':'gender',
                  '_age': 'age', '_sales': 'sales',
                  '_bmi': 'bmi'}

    def __init__(self, dictionary, salary, birthday):
        self.__dict__.update(dictionary)
        self._salary = salary
        self._birthday = birthday

    def get_all_data(self):
        employee_info = [self._emp_id, self._gender, self._age, self._sales, self._bmi, self._salary, self._birthday]
        return employee_info

