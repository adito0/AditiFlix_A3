from datetime import date, datetime

import pytest

from AditiFlix_App.domainmodel.user import User
from AditiFlix_App.domainmodel.review import Review
from AditiFlix_App.domainmodel.movielist import MovieList
from AditiFlix_App.domainmodel.movie import Movie
from AditiFlix_App.domainmodel.genre import Genre
from AditiFlix_App.domainmodel.director import Director
from AditiFlix_App.domainmodel.actor import Actor
from AditiFlix_App.adapters.movie_repository import RepositoryException

def test_add_get_user(in_memory_repo):
    assert in_memory_repo.get_user("pikachu") is None
    in_memory_repo.add_user(User("pikachu","three3"))
    assert in_memory_repo.get_user("pikachu")== User("pikachu","some password")

def test_add_get_review(in_memory_repo):
    rev = Review(Movie("Docker", 2009), "So great", 9.3)
    assert rev not in in_memory_repo.get_reviews()
    in_memory_repo.add_review(rev)
    assert rev in in_memory_repo.get_reviews()

def test_get_reviews_from_movies(in_memory_repo):
    rev = Review(in_memory_repo.get_movie("Split",2016),"Wow!",10.0)
    rev.timestamp = datetime.fromisoformat("2018-03-28 16:31:26")
    rev2 = Review(in_memory_repo.get_movie("Split",2016), "I love this movie so much!! It really makes you think", 9.0)
    rev2.timestamp = datetime.fromisoformat("2020-02-28 18:31:26")
    assert in_memory_repo.get_reviews_for_movie(in_memory_repo.get_movie("Split",2016)) == [rev2, rev]

def test_add_get_movie(in_memory_repo):
    movie = Movie("Lion", 2018)
    assert in_memory_repo.get_movie("Lion", 2018) == None
    in_memory_repo.add_movie(movie)
    assert in_memory_repo.get_movie("Lion", 2018) == movie

def test_get_movies_by_title(in_memory_repo):
    assert in_memory_repo.get_movies_by_title("Split") == [Movie("Split", 2016)]
    movie = Movie("Split", 2017)
    in_memory_repo.add_movie(movie)
    assert in_memory_repo.get_movies_by_title("Split") == [Movie("Split", 2016), Movie("Split", 2017)]

def test_get_number_of_movies(in_memory_repo):
    assert in_memory_repo.get_number_of_movies() == 13
    movie = Movie("Split", 2017)
    in_memory_repo.add_movie(movie)
    assert in_memory_repo.get_number_of_movies() == 14
    movie = Movie("Split", 2017)
    in_memory_repo.add_movie(movie)
    assert in_memory_repo.get_number_of_movies() == 14

def test_get_movies_for_genre(in_memory_repo):
    assert len(in_memory_repo.get_movies_for_genre("Adventure")) == 7
    assert Movie("Prometheus", 2012) in in_memory_repo.get_movies_for_genre("Adventure")
    assert Movie("Guardians of the Galaxy", 2014) in in_memory_repo.get_movies_for_genre("Adventure")
    assert Movie("Suicide Squad", 2016) in in_memory_repo.get_movies_for_genre("Adventure")
    assert in_memory_repo.get_movies_for_genre("Anime") == []

def test_get_movies_for_director(in_memory_repo):
    movie = Movie("Lion", 2018)
    movie.director = Director("Taika Waititi")
    in_memory_repo.add_movie(movie)
    assert Movie("Lion", 2018) in in_memory_repo.get_movies_for_director("Taika Waititi")
    assert len(in_memory_repo.get_movies_for_director("Taika Waititi")) == 1
    assert in_memory_repo.get_movies_for_director("Katy Perry") == []

def test_get_movies_for_actors(in_memory_repo):
    movie = Movie("Split", 2016)
    in_memory_repo.add_movie(movie)
    assert Movie("Suicide Squad", 2016) in in_memory_repo.get_movies_for_actor("Will Smith")
    assert len(in_memory_repo.get_movies_for_actor("Will Smith")) == 1
    assert in_memory_repo.get_movies_for_actor("Katy Perry") == []

def test_add_genre(in_memory_repo):
    assert Genre("Anime") not in in_memory_repo.get_genres()
    in_memory_repo.add_genre(Genre("Anime"))
    assert Genre("Anime") in in_memory_repo.get_genres()

def test_add_actor(in_memory_repo):
    assert Actor("Katy Perry") not in in_memory_repo.get_actors()
    in_memory_repo.add_actor(Actor("Katy Perry"))
    assert Actor("Katy Perry") in in_memory_repo.get_actors()

def test_add_genre(in_memory_repo):
    assert Director("Katy Perry") not in in_memory_repo.get_directors()
    in_memory_repo.add_director(Director("Katy Perry"))
    assert Director("Katy Perry") in in_memory_repo.get_directors()