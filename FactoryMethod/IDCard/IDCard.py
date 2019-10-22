from Product import Product


class IDCard(Product):

    def __init__(self, owner):
        print(owner + 'のカードを作ります。')
        self.owner = owner

    def use(self):
        print(self.owner + 'のカードを使います。')

    def getOwner(self):
        return self.owner
