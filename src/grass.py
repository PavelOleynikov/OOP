from src.models import Product


class LawnGrass(Product):
    """класс Трава газонная - наследник класса Product"""

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):  # метод сложения стоимости продуктов
        if type(other) is LawnGrass:
            cost_products = self.price * self.quantity + other.price * other.quantity
            return cost_products
        raise TypeError
