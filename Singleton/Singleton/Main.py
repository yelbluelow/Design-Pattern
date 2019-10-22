from Singleton import Singleton


def main():
    print('Start.')
    obj1 = Singleton()
    obj2 = Singleton()

    if (obj1 == obj2):
        print('obj1 and obj2 are the same instance')

    else:
        print('obj1 and obj2 are not the same instance')

    print('End.')

if __name__ == '__main__':
    main()
