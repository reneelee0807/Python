from abstract_factory_file import AbstractFactoryFile
from read_excel import ReadExcel
from save_excel import SaveExcel


class ExcelFactory(AbstractFactoryFile):
    @staticmethod
    def create_file_content():
        return ReadExcel()

    @staticmethod
    def create_save_file():
        return SaveExcel()
