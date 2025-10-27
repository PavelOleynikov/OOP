from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс - родитель для класса продуктов"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
