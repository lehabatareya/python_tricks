"""
Descriptors are classes to abstract the class attributes behavior.
This is the example descriptor from perfect presentation
'Python: Encapsulation with Descriptors'
by Luciano Ramalho
"""


class Quantity:
    """
    Descriptor class for nonnegative quantities
    Raises ValueError if you try to assign negative value to the attribute
    """
    __instance_counter = 0

    def __init__(self):
        self.field_name = '_' + self.__class__.__name__ + '_'
        self.__class__.__instance_counter += 1
        self.field_name += str(self.__instance_counter)

    def __set__(self, instance, value):
        """Sets only positive or 0 values. In case of negative value - error"""
        if value >= 0:
            setattr(instance, self.field_name, value)
        else:
            raise ValueError('Value must be > 0')

    def __get__(self, instance, owner):
        return getattr(instance, self.field_name)


class ShopItem(object):
    """
    Shop item with given quantity and given value
    """
    quantity = Quantity()
    value = Quantity()

    def __init__(self, description, quantity, value):
        self.description = description
        self.quantity = quantity
        self.value = value

    def get_cost(self):
        """Get the total cost of the shop item"""
        return self.quantity * self.value


if __name__ == '__main__':
    carrot = ShopItem("Carrots", 10, 13)
    print(f'Quantity = {carrot.quantity}, value = {carrot.value}')
    print(f'Total cost = {carrot.get_cost()}')
