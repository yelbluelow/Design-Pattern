from abc import ABCMeta, abstractmethod


class Factory(metaclass=ABCMeta):

    def create(self, owner):
        self.p = self.createProduct(owner)
        self.registerProduct(self.p)
        return self.p

    @abstractmethod
    def createProduct(self, owner):
        pass

    @abstractmethod
    def registerProduct(self, product):
        pass
