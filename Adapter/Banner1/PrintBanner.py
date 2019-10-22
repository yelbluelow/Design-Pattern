from Banner import Banner
from __Print import __Print


class PrintBanner(Banner, __Print):

    def __init__(self, string):
        super().__init__(string)

    def printWeak(self):
        self.showWithParen()

    def printStrong(self):
        self.showWithAster()
