from abc import ABCMeta, abstractmethod


# AbstractProductA
class ReadFiler(metaclass=ABCMeta):
    @abstractmethod
    def get_result(self):
        pass