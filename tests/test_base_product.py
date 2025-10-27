from src.base_product import BaseProduct
from src.models import Product


def test_product_implements_base_product():
    """Тест, что класс Product наследует от BaseProduct"""
    assert issubclass(Product, BaseProduct)
