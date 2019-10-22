from abc import ABCMeta, abstractmethod


class __Iterator(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def hasNext(self):
        pass

    @abstractmethod
    def next(self):
        pass
