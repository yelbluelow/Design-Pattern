import glob
from AbstractAccess import AbstractAccess


class TextAccess(AbstractAccess):

    def fetchFilePath(self):
        self.__path = glob.glob('*.txt')

    def fetchData(self):
        __data = open(self.__path[0], 'r')
        __data_temp = __data.readlines()
        self.__data = []
        for __record in __data_temp:
            self.__data.append(__record.split())

    def showDetail(self):
        print('〇text表示')
        for __record in self.__data:
            print('------------------------')
            print('名前：', __record[0])
            print('性別：', __record[1])
            print('生年月日', __record[2])
            print('------------------------')
