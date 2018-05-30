from abstract_factory_file import AbstractFactoryFile
from read_txt import ReadTxt
from save_txt import SaveTxt


class TXTFactory(AbstractFactoryFile):
    @staticmethod
    def create_file_content():
        return ReadTxt()

    @staticmethod
    def create_save_file():
        return SaveTxt()
