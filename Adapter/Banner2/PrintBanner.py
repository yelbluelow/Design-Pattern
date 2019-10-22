from Print import Print
from Banner import Banner


class PrintBanner(Banner):

    def __init__(self, string):
        super().__init__(string)
        self.__banner = Banner(string)

    def printWeak(self):
        self.__banner.showWithParen()

    def printStrong(self):
        self.__banner.showWithAster()
