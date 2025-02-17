class PrintMixin:
    """ Класс для вывода в консоль данных о созданном объекте класса product"""

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
