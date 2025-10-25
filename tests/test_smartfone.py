import pytest

from src.smartfone import Smartphone


def test_smartfone_init(smartphone1: Smartphone) -> None:
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"


def test_smartfone_add(smartphone1: Smartphone, smartphone2: Smartphone) -> None:
    assert smartphone1 + smartphone2 == 2580000


def test_smartfone_add_error(smartphone1: Smartphone) -> None:
    with pytest.raises(TypeError):
        result = smartphone1 + 1
