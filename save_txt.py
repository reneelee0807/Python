from save_filer import SaveFiler


# ConcreteProductB2
class SaveTxt(SaveFiler):
    @staticmethod
    def get_result(file_name, employee_list):
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