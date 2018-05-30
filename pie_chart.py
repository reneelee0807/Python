import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import numpy as np
from employee_database import EmployeeDatabase
from abstract_make_chart import AbstractMakeChart


class PieChart(AbstractMakeChart):
    def __init__(self):
        super().__init__()
        self.db = EmployeeDatabase()

    def create(self):
        employee_list = self.db.get_all_employee()
        labels = [emp[0] for emp in employee_list]
        sales = [emp[5] for emp in employee_list]

        plt.pie(sales, labels=labels, shadow=True)
        plt.axis('equal')
        plt.title("Sales by Salesperson")
        plt.show()
