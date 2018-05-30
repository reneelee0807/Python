from read_filer import ReadFiler


# ConcreteProductA1
class ReadTxt(ReadFiler):
    @staticmethod
    def get_result(file_name):
        with open(file_name, "r+") as fo:
            data = [line.split("$") for line in fo]
        return data
