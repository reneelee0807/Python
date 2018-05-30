from save_filer import SaveFiler
import os
import pandas as pd


# ConcreteProductB2
class SaveExcel(SaveFiler):
    @staticmethod
    def get_result(file_name, employee_list):
        special_char = "\|!#$%&/()=?»«@£§€{};'<>,"
        for character in file_name:
            if character in special_char:
                raise NameError
        if os.path.isfile(file_name):
            raise FileExistsError('file already exists, please rename')
        df = pd.DataFrame.from_records(employee_list)
        writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
        df.to_excel(writer, index=False, header=False, sheet_name='Sheet1')
        writer.save()
        print("Data is saved")
