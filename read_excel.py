from read_filer import ReadFiler
import pandas as pd


# ConcreteProductA1
class ReadExcel(ReadFiler):
    @staticmethod
    def get_result(file_name):
        special_char = "\|!#$%&/()=?»«@£§€{};'<>,"
        for character in file_name:
            if character in special_char:
                raise NameError
        xl = pd.ExcelFile(file_name)
        print(xl.sheet_names)
        print(xl.parse('Sheet1'))
        df = pd.read_excel(file_name, sheet_name='Sheet1')
        content = df.values.tolist()
        for employee in content:
            if not isinstance(employee[6], str):
                employee[6] = employee[6].strftime("%d-%m-%Y")
        print(content)
        return content