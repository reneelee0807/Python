import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import numpy as np
from employee_database import EmployeeDatabase
from abstract_make_chart import AbstractMakeChart


class SalesSalaryAvgBarChart(AbstractMakeChart):
    def __init__(self):
        super().__init__()
        self.db = EmployeeDatabase()
    # db = EmployeeDatabase()

    def create(self):
        ave_sales = self.db.get_ave_sales()
        ave_salary = self.db.get_ave_salary()
        objects = ('Average Sales', 'Average Salary')
        y_pos = np.arange(len(objects))
        performance = [ave_sales, ave_salary]
        if ave_sales < 0 or ave_salary < 0:
            raise ValueError("wrong value of the input")
        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('NZ Dollor')
        plt.title('Average Sales and Average Salary')
        plt.show()