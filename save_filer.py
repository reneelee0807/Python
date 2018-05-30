from abc import ABCMeta, abstractmethod


# AbstractProductB
class SaveFiler(metaclass=ABCMeta):
    @abstractmethod
    def get_result(self):
        pass
