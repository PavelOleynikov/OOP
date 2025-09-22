import pytest
from src.models import Product, Category


@pytest.fixture
def product1() -> Product:
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture
def category1(product1: Product) -> Category:
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1],
    )


def test_init_product(product1: Product) -> None:
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_init_category(category1: Category, product1: Product) -> None:
    assert category1.name == "Смартфоны"
    assert (
        category1.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category1.products == [product1]


def test_product_count() -> None:
    assert Category.product_count == 1


def test_category_count() -> None:
    assert Category.category_count == 1
