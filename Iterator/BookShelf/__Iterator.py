from abc import ABCMeta, abstractmethod


class __Iterator(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        raise Exception('abstract class')

    @abstractmethod
    def hasNext(self):
        raise Exception('hasNext() must be implemented')

    @abstractmethod
    def next(self):
        raise Exception('next() must be implemented')
