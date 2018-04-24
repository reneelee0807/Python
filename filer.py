import pandas as pd
import csv
import os


class Filer:
    """A class to load and sale data from CSV, XLSX and TXT file."""

    # Jonno's
    @staticmethod
    def read_excel(file_name):
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

    @staticmethod
    def save_excel(file_name, employee_list):
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

    # Renees:
    @staticmethod
    def read_csv(file_name):
        try:
            if os.path.isfile(file_name):
                with open(file_name, newline='') as file_data:
                    reader = csv.reader(file_data)
                    content = list(reader)
                    return content
            else:
                raise FileNotFoundError
        except NameError as e:
            print(e)
        except FileNotFoundError:
            raise FileNotFoundError('No such file or directory')
        except OSError:
            raise OSError('can not open the file', file_name)
        except IndexError as e:
            print(e)
        except TypeError as e:
            print('read_csv() missing 1 required argument: file_name')
        except Exception as e:
            print('there is something wrong', file_name)

    @staticmethod
    def check_file_name(file_name):
        special_char = "\|!#$%&/()=?»«@£§€{};'<>,"
        for character in file_name:
            if character in special_char:
                raise NameError
            else:
                return True


    def save_csv(self, file_name, employee_list):
        try:
            if(self.check_file_format(file_name) == True):
                if os.path.isfile(file_name):
                    raise FileExistsError('file already exists')
                df = pd.DataFrame(employee_list)
                df.to_csv(file_name, index=False, header=False)
                print("Data is saved")
        except OSError as e:
            print(e)
        except Exception as e:
            print('can not save the file', file_name)

    # Chamillas:
    @staticmethod
    def read_txt(file_name):
        with open(file_name, "r+") as fo:
            data = [line.split("$") for line in fo]
        return data

    @staticmethod
    def save_txt_file(file_name, employee_list):
        """

        """
        try:
            with open(file_name, "w") as f:
                for item in employee_list:
                    for i in item:
                        f.write(str(i) + '$')
                    f.write("\n")
                f.close()
                print("Data saved to file")
        except NameError as e:
            print(e)
        except OSError:
            print("Can not save file", file_name)
        except IndexError as e:
            print(e)
        except Exception as e:
            print(e)
        except:
            print("Something went wrong")


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
