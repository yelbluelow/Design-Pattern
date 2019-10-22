from Factory import Factory
from IDCard import IDCard


class IDCardFactory(Factory):

    def __init__(self):
        self.owners = []

    def createProduct(self, owner):
        return IDCard(owner)

    def registerProduct(self, product):
        self.owners.append(product.getOwner())

    def gerOwners(self):
        return self.owners
