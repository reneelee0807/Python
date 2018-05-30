from save_filer import SaveFiler
import csv
import os
import pandas as pd


# ConcreteProductB2
class SaveCSV(SaveFiler):
    @staticmethod
    def check_file_name(file_name):
        special_char = "\|!#$%&/()=?»«@£§€{};'<>,"
        for character in file_name:
            if character in special_char:
                raise NameError
            else:
                return True

    @staticmethod
    def check_file_exists(file_name):
        if os.path.isfile(file_name):
            raise FileExistsError('file already exists')
        else:
            return True

    def get_result(self, file_name, employee_list):
        try:
            if self.check_file_name(file_name):
                if self.check_file_exists(file_name):
                    df = pd.DataFrame(employee_list)
                    df.to_csv(file_name, index=False, header=False)
                    print("Data is saved")
        except OSError as e:
            print(e)
        except Exception as e:
            print('can not save the file', file_name)