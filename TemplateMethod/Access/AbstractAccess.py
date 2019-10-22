from abc import ABCMeta, abstractmethod


class AbstractAccess(metaclass=ABCMeta):

    @abstractmethod
    def fetchFilePath(self):
        pass

    @abstractmethod
    def fetchData(self):
        pass

    @abstractmethod
    def showDetail(self):
        pass

    def access(self):
        self.fetchFilePath()
        self.fetchData()
        self.showDetail()
