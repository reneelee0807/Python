from abstract_factory_file import AbstractFactoryFile
from read_csv import ReadCSV
from save_csv import SaveCSV


class CSVFactory(AbstractFactoryFile):
    @staticmethod
    def create_file_content():
        return ReadCSV()

    @staticmethod
    def create_save_file():
        return SaveCSV()
