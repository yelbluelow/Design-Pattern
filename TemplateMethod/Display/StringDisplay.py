from AbstractDisplay import AbstractDisplay
import unicodedata


class StringDisplay(AbstractDisplay):

    def __init__(self, string):
        self.string = string
        self.width = self.get_east_asian_width_count(self.string)

    def open(self):
        self.printLine()

    def print(self):
        print('|' + self.string + '|')

    def close(self):
        self.printLine()

    def printLine(self):
        line = '+'
        for _ in range(self.width):
            line += '-'
        line += '+'
        print(line)

    def get_east_asian_width_count(self, text):
        count = 0
        for c in text:
            if unicodedata.east_asian_width(c) in 'FWA':
                count += 2
            else:
                count += 1
        return count
