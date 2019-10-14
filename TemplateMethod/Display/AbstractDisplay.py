# -*- coding: utf-8 -*-


from abc import ABCMeta, abstractmethod


class AbstractDisplay(metaclass=ABCMeta):
    @abstractmethod
    def open(self):
        pass

    def print(self):
        pass

    def close(self):
        pass

    def display(self):
        self.open()
        for _ in range(5):
            self.print()
        self.close()
