from __Aggregate import __Aggregate
from BookShelfIterator import BookShelfIterator


class BookShelf(__Aggregate):

    def __init__(self):
        self.__books = []
        self.__last = 0

    def getBookAt(self, index):
        return self.__books[index]

    def appendBook(self, book):
        self.__books.append(book)
        self.__last += 1

    def getLength(self):
        return self.__last

    def iterator(self):
        return BookShelfIterator(self)
