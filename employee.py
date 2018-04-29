class Employee:
    """Base class for all Employees"""

    dictionary = {'self._emp_id': 'emp_id', 'self._gender':'gender'}

    def __init__(self, dictionary, age, sales, bmi, salary, birthday):
        self.__dict__.update(dictionary)
        self._age = age
        self._sales = sales
        self._bmi = bmi
        self._salary = salary
        self._birthday = birthday

    def get_all_data(self):
        employee_info = [self._emp_id, self._gender, self._age, self._sales, self._bmi, self._salary, self._birthday]
        return employee_info

