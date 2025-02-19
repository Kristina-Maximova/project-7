from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """ Абстрактный класс, задающий шаблон для класса продуктов"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        """ Oбязывает определять метод добавления продуктов в дочерних классах """
        pass


class BaseCategory(ABC):
    """ Абстрактный класс, шаблон для работ с категориями продуктов"""

    @abstractmethod
    def add_product(self, *args, **kwargs):
        """ Обязывает определять метод добавления объекта класса product в категорию"""