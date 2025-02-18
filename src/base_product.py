from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """ Абстрактный класс, задающий шаблон для класса продуктов"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        """ Oбязывает определять метод добавления продуктов в дочерних классах """
        pass
