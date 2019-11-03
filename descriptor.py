"""
Descriptors are classes to abstract the class instance attributes behavior.
This is the example descriptor from perfect presentation:
'Python: Encapsulation with Descriptors'
by Luciano Ramalho
"""


class Quantity:
    """
    Descriptor class for nonzero quantities
    """
    def __init__(self):
        self.field_name = ''

    def __set__(self, instance, value):
        pass

    def __get__(self, instance, owner):
        pass


class ShopItem:
    """
    Simple class of shop item with given weight and given
    """
    def __init__(self, weight, value):
        self.quantity = Quantity()
        self.value = Quantity()

    def get_cost(self):
        """Get the total cost of the shop item"""
        return self.quantity * self.value


if __name__ == '__main__':
    carrot = ShopItem(10, 13)
