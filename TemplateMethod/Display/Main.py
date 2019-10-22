from CharDisplay import CharDisplay
from StringDisplay import StringDisplay


def main():
    d1 = CharDisplay('H')
    d2 = StringDisplay('Hello, World.')
    d3 = StringDisplay('こんにちは。')

    d1.display()
    d2.display()
    d3.display()

if __name__ == '__main__':
    main()
