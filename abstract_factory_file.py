from abc import ABCMeta, abstractmethod


class AbstractFactoryFile(metaclass=ABCMeta):
    @abstractmethod
    def create_file_content(self):
        pass

    @abstractmethod
    def create_save_file(self):
        pass