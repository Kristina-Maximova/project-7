class PrintMixin:
    """ Класс для вывода в консоль данных о созданном объекте класса product"""

    def __init__(self):
        """ Выводит в консоль данные о созданном объекте"""
        print(repr(self))

    def __repr__(self):
        """ Метод задает формат вывода при вызове repr """
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
