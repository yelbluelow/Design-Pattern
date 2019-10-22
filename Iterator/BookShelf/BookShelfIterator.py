from __Iterator import __Iterator


class BookShelfIterator(__Iterator):

    def __init__(self, bookShelf):
        self.__bookShelf = bookShelf
        self.__index = 0

    def hasNext(self):
        if (self.__index < self.__bookShelf.getLength()):
            return True
        else:
            return False

    def next(self):
        book = self.__bookShelf.getBookAt(self.__index)
        self.__index += 1
        return book
