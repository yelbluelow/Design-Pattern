from IDCardFactory import IDCardFactory


def main():
    factory = IDCardFactory()
    card1 = factory.create('Ichiro')
    card2 = factory.create('Jiro')
    card3 = factory.create('Saburo')
    card1.use()
    card2.use()
    card3.use()

if __name__ == '__main__':
    main()
