from src.models import Product


class Smartphone(Product):
    """класс Смартфон - наследник класса Product"""

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):  # метод сложения стоимости продуктов
        if type(other) is Smartphone:
            cost_products = self.price * self.quantity + other.price * other.quantity
            return cost_products
        raise TypeError
