import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import numpy as np
from employee_database import EmployeeDatabase
from abstract_make_chart import AbstractMakeChart


class SalesBarChart(AbstractMakeChart):
    def __init__(self):
        super().__init__()
        self.db = EmployeeDatabase()

    def create(self):
        employee_list = self.db.get_all_employee()
        objects = [item[0] for item in employee_list]
        sales = [item[3] for item in employee_list]
        y_pos = np.arange(len(objects))

        plt.bar(y_pos, sales, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel("Sales")
        plt.xlabel("Salesperson by ID")
        plt.title("Sales By Salesperson")

        plt.show()
