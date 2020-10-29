from AditiFlix_App.domainmodel.director import Director

import pytest


@pytest.fixture
def director():
    return Director('Taika Waititi')


def test_init(director):
    assert director.director_full_name == 'Taika Waititi'
    director1 = Director("Taika Waititi")
    assert repr(director1) == "<Director Taika Waititi>"
    director2 = Director("")
    assert director2.director_full_name is None
    director3 = Director(42)
    assert director3.director_full_name is None
    assert repr(director2) == "<Director None>"
    assert repr(director3) == "<Director None>"


def test_compare():
    director1 = Director("Taika Waititi")
    director2 = Director("Taika Waititi")
    assert director1 == director2
    director2 = 4
    assert director1 != director2
    director1 = Director("")
    director2 = Director(45)
    assert director1 == director2


def test_lt():
    director1 = Director("Taika Waititi")
    director2 = Director("Aika Waititi")
    assert director1 > director2


def test_hash():
    director1 = Director("Taika Waititi")
    director2 = Director("Taika Waititi")
    assert hash(director1) == hash(director2)
    director2 = Director("Taika Waititj")
    assert hash(director1) != hash(director2)
    dict1 = dict()
    dict1[director1] = director2
    assert dict1[director1] == director2
    assert repr(dict1[director1]) == "<Director Taika Waititj>"
    director1 = Director("")
    director2 = Director(9)
    dict1[director1] = director2
    assert dict1[director1] == director2
    assert repr(dict1[director1]) == "<Director None>"
