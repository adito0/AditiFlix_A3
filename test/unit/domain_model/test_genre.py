from AditiFlix_App.domainmodel.genre import Genre

import pytest


@pytest.fixture
def genre():
    return Genre('Drama')


def test_init(genre):
    assert genre.genre_name == 'Drama'
    genre1 = Genre("Comedy")
    assert repr(genre1) == "<Genre Comedy>"
    genre2 = Genre("")
    assert genre2.genre_name is None
    genre3 = Genre(42)
    assert genre3.genre_name is None
    assert repr(genre2) == "<Genre None>"
    assert repr(genre3) == "<Genre None>"


def test_compare():
    genre1 = Genre("Comedy")
    genre2 = Genre("Comedy")
    assert genre1 == genre2
    genre2 = 4
    assert genre1 != genre2
    genre1 = Genre("")
    genre2 = Genre(45)
    assert genre1 == genre2
    genre1 = Genre("Comedy")
    genre2 = Genre("comedy")
    assert genre1 != genre2


def test_lt():
    genre1 = Genre("Comedy")
    genre2 = Genre("Drama")
    assert genre1 < genre2
    assert genre2 > genre1


def test_le():
    genre1 = Genre("Comedy")
    genre2 = Genre("Drama")
    assert genre1 <= genre2
    assert genre2 >= genre1
    genre1 = Genre("Comedy")
    genre2 = Genre("Comedy")
    assert genre1 <= genre2
    assert genre2 >= genre1


def test_hash():
    genre1 = Genre("Comedy")
    genre2 = Genre("Comedy")
    assert hash(genre1) == hash(genre2)
    genre2 = Genre("Comedz")
    assert hash(genre1) != hash(genre2)
    dict1 = dict()
    dict1[genre1] = genre2
    assert dict1[genre1] == genre2
    assert repr(dict1[genre1]) == "<Genre Comedz>"
    genre1 = Genre("")
    genre2 = Genre(7)
    dict1[genre1] = genre2
    assert dict1[genre1] == genre2
    assert repr(dict1[genre1]) == "<Genre None>"