from abc import ABCMeta, abstractmethod


class __Aggregate(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def iterator(self):
        pass
