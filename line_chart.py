import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import numpy as np
from employee_database import EmployeeDatabase
from abstract_make_chart import AbstractMakeChart


class LineChart(AbstractMakeChart):
    def __init__(self):
        super().__init__()
        self.db = EmployeeDatabase()

    def create(self):
        employee_list = self.db.get_all_employee()
        # our X values:
        emp_id = [emp[0] for emp in employee_list]
        # our Y values:
        sales_values = [emp[3] for emp in employee_list]
        plt.plot(emp_id, sales_values, '-b', label="A simple line")
        plt.legend(loc='upper left')
        plt.title("Sales Value for Employees")
        plt.xlabel('Employee ID')
        plt.ylabel('Sales')
        plt.show()

        plt.plot(emp_id, sales_values, 'bo')
        plt.show()
