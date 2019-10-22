from TextAccess import TextAccess
from CsvAccess import CsvAccess


def main():
    a_text = TextAccess()
    a_csv = CsvAccess()

    a_text.access()
    a_csv.access()

if __name__ == '__main__':
    main()
