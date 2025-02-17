from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """ Абстрактный класс, задающий шаблон для класса продуктов"""
    @abstractmethod
    def __init__(self):
        """ метод обязывает определять конструктор класса в дочерних классах """
        super().__init__()
        pass