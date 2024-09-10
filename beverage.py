class Beverage:

    def __init__(self, name, size, price):
        self.__name = name
        self.__size = size
        self.__price = price

    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price
