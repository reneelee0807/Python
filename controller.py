from employee_database import EmployeeDatabase
from filer import Filer
from validator import Validator
from chart_maker import ChartMaker
from txt_factory import TXTFactory
from csv_factory import CSVFactory
from excel_factory import ExcelFactory
from read_csv import ReadCSV
from sales_salary_avg_bar_chart import SalesSalaryAvgBarChart
from chart import Chart
from pie_chart import PieChart
from line_chart import LineChart
from sales_bar_chart import SalesBarChart


class Controller:
    def __init__(self):
        self.cf = CSVFactory()
        self.f = Filer()
        self.v = Validator()
        self.db = EmployeeDatabase()
        self.chart = ChartMaker()


    @staticmethod
    def load_filer(factory, file):
        return factory.create_file_content().get_result(file)
    
    @staticmethod
    def save_filer(factory, file, employee_list):
        return factory.create_save_file().get_result(file, employee_list)

    # Jono's
    def load_file(self, file):
        try:
            if ".csv" in file[-4:]:
                content = self.load_filer(CSVFactory(), file)

            elif ".xlsx" in file[-5:]:
                content = self.load_filer(ExcelFactory(), file)
            elif ".txt" in file[-4:]:
                content = self.load_filer(TXTFactory(), file)
            else:
                message = "incorrect format please see help load"
                raise NameError(message)
            validated_employees = self.validate_items(content)
            return validated_employees
        except NameError as e:
            print(e)
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print(e)

    def validate_items(self, content):
        valid_employees = []
        invalid_employees = []
        for employee in content:
            item = self.v.validate_all(employee)
            if False in item:
                invalid_employees.append(employee)
            else:
                valid_employees.append(employee)
            emp = {'Valid': valid_employees, 'Invalid': invalid_employees}
        return emp

    def add_to_database(self, content_list):
        for item in content_list:
            self.db.insert_employee(item)

    def get_all_employees(self):
        try:
            employees = self.db.get_all_employee()
            if len(employees) > 0:
                return employees
            else:
                raise IndexError
        except IndexError:
            print("No employees in database")
        except Exception as e:
            print(e)

    # renee
    def print_chart_average(self):
        bar_chart = Chart(SalesSalaryAvgBarChart())
        bar_chart.make_chart()

    def print_chart_sales(self):
        bar_chart = Chart(SalesBarChart())
        bar_chart.make_chart()

    def print_chart_pie(self):
        pie_chart = Chart(PieChart())
        pie_chart.make_chart()

    def print_chart_line(self):
        line_chart = Chart(LineChart())
        line_chart.make_chart()

    # Chami
    def save_file(self, file_format, employee_list):
        try:
            if ".csv" in file_format:
                content = self.save_filer(CSVFactory(), file_format, employee_list)
            elif ".xlsx" in file_format:
                content = self.save_filer(ExcelFactory(), file_format, employee_list)
            elif ".txt" in file_format:
                content = self.save_filer(TXTFactory(), file_format, employee_list)
            else:
                raise NameError("can not save that file type")
        except NameError as e:
            print(e)

    def save_invalid(self, invalid_employees):
        try:
            self.f.save_txt_file("invalid.csv", invalid_employees)
        except:
            print("Whoops something went wrong")
