from AditiFlix_App.domainmodel.movie import Movie
from AditiFlix_App.domainmodel.director import Director
from AditiFlix_App.domainmodel.genre import Genre
from AditiFlix_App.domainmodel.actor import Actor

import pytest


@pytest.fixture
def movie():
    return Movie('Up', 2009)


def test_init(movie):
    assert movie.title == 'Up'
    assert movie.release_year == 2009
    movie1 = Movie("Enchanted", 2012)
    assert repr(movie) == "<Movie Up, 2009>"
    assert repr(movie1) == "<Movie Enchanted, 2012>"
    movie1 = Movie("Enchanted", 'a')
    assert repr(movie1) == "<Movie Enchanted, None>"
    movie1 = Movie("Enchanted", 10)
    assert repr(movie1) == "<Movie Enchanted, None>"
    movie1 = Movie("Enchanted", 2021)
    assert repr(movie1) == "<Movie Enchanted, None>"
    movie2 = Movie("", 4)
    assert movie2.title is None
    assert repr(movie2) == "<Movie None, None>"
    movie3 = Movie(42, 2000)
    assert movie3.title is None
    assert repr(movie3) == "<Movie None, 2000>"


def test_attribute_access(movie):
    # Checking Movie title
    movie.title = ""
    assert repr(movie) == "<Movie None, 2009>"
    movie.title = "Annabelle"
    assert repr(movie) == "<Movie Annabelle, 2009>"
    movie.title = 5
    assert repr(movie) == "<Movie None, 2009>"
    movie.title = "Annabelle"

    # Checking Movie release year
    movie.release_year = 0
    assert repr(movie) == "<Movie Annabelle, None>"
    movie.release_year = 2021
    assert repr(movie) == "<Movie Annabelle, None>"
    movie.release_year = 2016
    assert repr(movie) == "<Movie Annabelle, 2016>"
    movie.release_year = 'a'
    assert repr(movie) == "<Movie Annabelle, None>"

    # Checking Movie description
    movie.description = 0
    assert movie.description is None
    movie.description = ""
    assert movie.description is None
    movie.description = "Test-description"
    assert movie.description == "Test-description"

    # Checking Movie runtime
    movie.runtime_minutes = "a"
    assert movie.runtime_minutes is None
    with pytest.raises(ValueError):
        movie.runtime_minutes = -14
    movie.runtime_minutes = 130
    assert movie.runtime_minutes == 130

    # Checking Movie Director
    movie.director = 3
    assert repr(movie.director) == "None"
    movie.director = Director(3)
    assert repr(movie.director) == "<Director None>"
    director = Director("Peter Jackson")
    movie.director = director
    assert movie.director == Director("Peter Jackson")
    movie.director = Director("")
    assert repr(movie.director) == "<Director None>"

    # Checking Movie Votes
    movie.votes = "a"
    assert movie.votes is None
    with pytest.raises(ValueError):
        movie.votes = -1
    movie.votes = 10
    assert movie.votes == 10

    # Checking Movie Rating
    movie.rating = "a"
    assert movie.rating is None
    with pytest.raises(ValueError):
        movie.rating = 11
    with pytest.raises(ValueError):
        movie.rating = -1
    movie.rating = 10
    assert movie.rating == 10

    # Checking Movie Rating after changing to 0 votes
    movie.votes = 0
    print(movie.rating)
    assert movie.rating is None
    movie.rating = 10
    assert movie.rating is None


def test_add_rating(movie):
    movie.votes = 10
    movie.rating = 8.8
    movie.add_rating(4)
    assert movie.votes == 11
    assert movie.rating == 8.4


def test_add_remove_actor(movie):
    movie.add_actor(Actor("Will Smith"))
    movie.add_actor(Actor(""))
    movie.add_actor(Actor(3))
    movie.add_actor(4)
    movie.add_actor(Actor("Daniel Radcliff"))
    assert movie.actors == [Actor("Will Smith"), Actor("Daniel Radcliff")]
    movie.remove_actor(Actor("Daniel Radcliff"))
    assert movie.actors == [Actor("Will Smith")]
    movie.remove_actor(Actor("Daniel Radcliff"))
    assert movie.actors == [Actor("Will Smith")]
    movie.remove_actor(Actor("Will Smith"))
    movie.remove_actor(4)
    movie.remove_actor(Actor(""))
    assert movie.actors == []
    movie.remove_actor(Actor("Will Smith"))
    assert movie.actors == []


def test_add_remove_genre(movie):
    movie.add_genre(Genre("Comedy"))
    movie.add_genre(Genre(""))
    movie.add_genre(Genre(3))
    movie.add_genre(4)
    movie.add_genre(Genre("Drama"))
    assert movie.genres == [Genre("Comedy"), Genre("Drama")]
    movie.remove_genre(Genre("Comedy"))
    assert movie.genres == [Genre("Drama")]
    movie.remove_genre(Genre("Comedy"))
    assert movie.genres == [Genre("Drama")]
    movie.remove_genre(Genre("Drama"))
    movie.remove_genre(Genre("Drama"))
    movie.remove_genre(4)
    movie.remove_genre(Genre(""))
    assert movie.genres == []
    movie.remove_genre(Genre("Drama"))
    assert movie.actors == []

def test_eq(movie):
    movie1 = Movie("Up", 2009)
    movie2 = Movie("Upp", 2009)
    movie3 = Movie("Up", 2019)
    assert movie == movie1
    assert movie != movie2
    assert movie != movie3
    movie2 = 4
    assert movie != movie2
    movie1 = Movie("", 2009)
    movie2 = Movie(45, 2009)
    movie3 = Movie("Hello", "f")
    movie4 = Movie("Hello", 1888)
    assert movie != movie1
    assert movie != movie2
    assert movie2 == movie1
    assert movie != movie3
    assert movie3 == movie4

def test_lt(movie):
    movie1 = Movie("", 2009)
    movie2 = Movie(45, 2009)
    movie3 = Movie("Hello", "f")
    movie4 = Movie("Hello", 1888)
    movie5 = Movie("Hello", 2009)
    movie6 = Movie("Goodbye", 2019)
    movie7 = Movie("Hello", 2019)
    assert movie5 < movie7
    assert movie5 > movie6
    assert movie7 > movie6
    assert (movie1 > movie) is None
    assert (movie2 > movie) is None
    assert movie > movie3
    assert movie > movie4


def test_hash():
    movie1 = Movie("HI", 1998)
    movie2 = Movie("HI", 1998)
    assert hash(movie1) == hash(movie2)
    movie2 = Movie("HI", 1997)
    assert hash(movie1) != hash(movie2)
    movie2 = Movie("HJ", 1998)
    assert hash(movie1) != hash(movie2)
    dict1 = dict()
    dict1[movie1] = movie2
    assert dict1[movie1] == movie2
    assert repr(dict1[movie1]) == "<Movie HJ, 1998>"
    movie1 = Movie("", 2009)
    movie2 = Movie(45, 2009)
    movie3 = Movie("Hello", "f")
    movie4 = Movie("Hello", 1888)
    dict1[movie1] = movie2
    dict1[movie3] = movie4
    assert dict1[movie1] == movie2
    assert repr(dict1[movie1]) == "<Movie None, 2009>"
    assert dict1[movie3] == movie4
    assert repr(dict1[movie3]) == "<Movie Hello, None>"


