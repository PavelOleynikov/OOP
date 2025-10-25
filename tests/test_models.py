import pytest

from src.models import Category, Product


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
    expected_string = (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )
    assert category1.products == expected_string


def test_product_count() -> None:
    assert Category.product_count == 2


def test_category_count() -> None:
    assert Category.category_count == 1


def test_new_product_property(new_product) -> None:
    assert new_product["name"] == "Samsung Galaxy S23 Ultra"
    assert new_product["description"] == "256GB, Серый цвет, 200MP камера"
    assert new_product["price"] == 180000.0
    assert new_product["quantity"] == 5


def test_new_price_setter() -> None:
    new_price = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    assert new_price.price == 123000.0


def test_products_property(product1: Product, category1: Category) -> None:
    result = category1.products
    expected = (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )

    assert result == expected


def test_product_str(product1: Product) -> None:
    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(product1: Product, product2: Product) -> None:
    assert product1 + product2 == 2580000.0


def test_category_str(category1: Category) -> None:
    assert str(category1) == "Смартфоны, количество продуктов: 13 шт."


def test_new_product(new_product) -> None:
    assert new_product == {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }


def test_add_product_error(category1: Category) -> None:
    with pytest.raises(TypeError):
        category1.add_product("Invalid product")
