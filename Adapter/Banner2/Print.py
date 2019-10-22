from abc import ABCMeta, abstractmethod


class Print(metaclass=ABCMeta):

    @abstractmethod
    def printWeak(self):
        pass

    @abstractmethod
    def printStrong(self):
        pass
