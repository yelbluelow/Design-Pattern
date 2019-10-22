import glob
import pandas as pd
from AbstractAccess import AbstractAccess


class CsvAccess(AbstractAccess):

    def fetchFilePath(self):
        self.__path = glob.glob('*.csv')

    def fetchData(self):
        self.__data = pd.read_csv(self.__path[0])

    def showDetail(self):
        print('〇csv表示')
        for i in range(len(self.__data)):
            print('========================')
            print('名前：', self.__data.iloc[i]['name'])
            print('性別：', self.__data.iloc[i]['sex'])
            print('生年月日', self.__data.iloc[i]['birthday'])
            print('========================')
