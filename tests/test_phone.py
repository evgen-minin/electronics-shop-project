import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture()
def phone1():
    return Phone("IPhone 14", 120000, 5, 2)


def test_phone(phone1):
    assert phone1.name == "IPhone 14"
    assert phone1.price == 120000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2


def test_set_phone_number_of_sim_wrong_value(phone1):
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0


def test__str__(phone1):
    assert str(phone1) == 'IPhone 14'


def test__repr__(phone1):
    assert repr(phone1) == "Phone('IPhone 14', 120000, 5, 2)"


def test_phone__add__(phone1):
    phone2 = Phone("Samsung", 80000, 15, 10)
    assert phone1 + phone2 == 20


def test_add(phone1):
    with pytest.raises(TypeError):
        phone1 + 10
