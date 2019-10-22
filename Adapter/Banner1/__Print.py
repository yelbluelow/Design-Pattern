from abc import ABCMeta, abstractmethod


class __Print(metaclass=ABCMeta):

    @abstractmethod
    def printWeak(self):
        pass
    
    @abstractmethod
    def printStrong(self):
        pass
