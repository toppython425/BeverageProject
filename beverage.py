class Beverage:
    """Добавлен базовый класс для газировки"""
    def __init__(self, name, size, price):
        self.__name = name
        self.__size = size
        self.__price = price

    """Добавлены геттеры"""
    def get_name(self):
        return self.__name

    def get_size(self):
        return self.__size

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def describe(self):
        """Метод для выдачи информации о продукции"""
        return f"Газировка: {self.get_name()}, объем: {self.get_size()}, цена: {self.get_price()}"


class Soda(Beverage):
    """Добавлен подкласс"""
    def __init__(self, name, size, price, flavour):
        super().__init__(name, size, price)
        self.__flavour = flavour
    
    def get_flavour(self):
        """Добавлен геттер для нового поля подкласса"""
        return self.__flavour

    def describe(self):
        """Расширен метод базового класса"""
        return f"{super().describe()}, вкус: {self.get_flavour()}"


class DietSoda(Soda):

    def describe(self):
        return f"{super().describe()}, фича: Диетическая!"
