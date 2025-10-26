from src.models import Product
from src.base_product import BaseProduct


def test_product_implements_base_product():
    """Тест, что класс Product наследует от BaseProduct"""
    assert issubclass(Product, BaseProduct)
