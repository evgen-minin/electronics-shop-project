"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200000


def test_apply_discount(item1):
    item1.apply_discount()
    assert item1.price == 10000

    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0


def test_name(item1):
    with pytest.raises(ValueError):
        item1.name = 'СуперСмартфон'
    item1.name = "Телефон"
    assert item1.name == 'Телефон'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'
