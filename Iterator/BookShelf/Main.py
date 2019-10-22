from BookShelf import BookShelf
from Book import Book


def main():

    bookshelf = BookShelf()
    bookshelf.appendBook(Book("Around the World in 80 Days"))
    bookshelf.appendBook(Book("Bible"))
    bookshelf.appendBook(Book("Cinderella"))
    bookshelf.appendBook(Book("Daddy-Long-Legs"))
    it = bookshelf.iterator()
    while it.hasNext():
        book = it.next()
        print(book.getName())

if __name__ == '__main__':
    main()


# referrence
# https://ksk77.blogspot.com/2010/11/1-iterator.html
