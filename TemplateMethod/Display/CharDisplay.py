from AbstractDisplay import AbstractDisplay


class CharDisplay(AbstractDisplay):

    def __init__(self, ch):
        self.ch = ch

    def open(self):
        print('<<')

    def print(self):
        print(self.ch)

    def close(self):
        print('>>')
