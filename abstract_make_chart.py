from abc import ABCMeta, abstractmethod


class AbstractMakeChart(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def create(self):
        pass
