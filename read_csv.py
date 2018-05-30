from read_filer import ReadFiler
import csv
import os


# ConcreteProductA2
class ReadCSV(ReadFiler):
    @staticmethod
    def get_result(file_name):
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