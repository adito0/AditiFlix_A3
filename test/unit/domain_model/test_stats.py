# from AditiFlix_App.domainmodel.movie import Movie
# from AditiFlix_App.domainmodel.director import Director
# from AditiFlix_App.domainmodel.genre import Genre
# from AditiFlix_App.domainmodel.actor import Actor
# from AditiFlix_App.domainmodel.user import User
# from AditiFlix_App.domainmodel.stats import Stats
# from AditiFlix_App.adapters.datafilereaders.movie_file_csv_reader import MovieFileCSVReader
#
# import pytest
#
#
# @pytest.fixture
# def stats():
#     movie = Movie('Up', 2009)
#     movie.add_actor(Actor("Will Smith"))
#     movie.add_actor(Actor("Daniel Radcliff"))
#     movie.add_genre(Genre("Comedy"))
#     movie.add_genre(Genre("Drama"))
#     director = Director("Peter Jackson")
#     movie.director = director
#
#     movie1 = Movie('Down', 2013)
#     movie1.add_actor(Actor("Tom Cruise"))
#     movie1.add_actor(Actor("Selena Gomez"))
#     movie1.add_genre(Genre("Comedy"))
#     movie1.add_genre(Genre("Romance"))
#     director = Director("Peter Jackson")
#     movie1.director = director
#
#     movie2 = Movie('Boom', 1999)
#     movie2.add_actor(Actor("Will Smith"))
#     movie2.add_actor(Actor("Tom Cruise"))
#     movie2.add_genre(Genre("Comedy"))
#     movie2.add_genre(Genre("Action"))
#     director = Director("Taika Waititi")
#     movie2.director = director
#
#     user = User("aram", "one1")
#     user.watch_movie(movie)
#     user.watch_movie(movie1)
#     user.watch_movie(movie2)
#
#     stats = Stats(user)
#     return stats
#
#
# def stat_class():
#     movie = Movie('Up', 2009)
#     movie.add_actor(Actor("Will Smith"))
#     movie.add_actor(Actor("Daniel Radcliff"))
#     movie.add_genre(Genre("Comedy"))
#     movie.add_genre(Genre("Drama"))
#     director = Director("Peter Jackson")
#     movie.director = director
#
#     movie1 = Movie('Down', 2013)
#     movie1.add_actor(Actor("Tom Cruise"))
#     movie1.add_actor(Actor("Selena Gomez"))
#     movie1.add_genre(Genre("Comedy"))
#     movie1.add_genre(Genre("Romance"))
#     director = Director("Peter Jackson")
#     movie1.director = director
#
#     movie2 = Movie('Boom', 1999)
#     movie2.add_actor(Actor("Will Smith"))
#     movie2.add_actor(Actor("Tom Cruise"))
#     movie2.add_genre(Genre("Comedy"))
#     movie2.add_genre(Genre("Action"))
#     director = Director("Taika Waititi")
#     movie2.director = director
#
#     user1 = User("aram", "one1")
#     user1.watch_movie(movie)
#     user1.watch_movie(movie1)
#     user1.watch_movie(movie2)
#
#     stats = Stats(user1)
#     return stats
#
#
# def test_init(stats):
#     assert stats.user == User("aram", "one1")
#     assert stats.watched_movies == [Movie("Up", 2009), Movie("Down", 2013), Movie("Boom", 1999)]
#     assert stats.watched_actors == {Actor("Will Smith"): 2, Actor("Daniel Radcliff"): 1, Actor("Selena Gomez"): 1,
#                                     Actor("Tom Cruise"): 2}
#     assert stats.watched_directors == {Director("Peter Jackson"): 2, Director("Taika Waititi"): 1}
#     assert stats.watched_genres == {Genre("Comedy"): 3, Genre("Romance"): 1, Genre("Drama"): 1, Genre("Action"): 1}
#
#
# def test_update(stats):
#     movie2 = Movie('Brain', 2002)
#     movie2.add_actor(Actor("Julia Roberts"))
#     movie2.add_actor(Actor("Tom Cruise"))
#     movie2.add_genre(Genre("Sci-Fi"))
#     movie2.add_genre(Genre("Action"))
#     director = Director("Christopher Nolan")
#     movie2.director = director
#
#     stats.user.watch_movie(movie2)
#     stats.update_watched_lists()
#
#     assert stats.user == User("aram", "one1")
#     assert stats.watched_movies == [Movie("Up", 2009), Movie("Down", 2013), Movie("Boom", 1999), Movie("Brain", 2002)]
#     assert stats.watched_actors == {Actor("Will Smith"): 2, Actor("Daniel Radcliff"): 1, Actor("Selena Gomez"): 1,
#                                     Actor("Tom Cruise"): 3, Actor("Julia Roberts"): 1}
#     assert stats.watched_directors == {Director("Peter Jackson"): 2, Director("Taika Waititi"): 1,
#                                        Director("Christopher Nolan"): 1}
#     assert stats.watched_genres == {Genre("Comedy"): 3, Genre("Romance"): 1, Genre("Drama"): 1, Genre("Action"): 2,
#                                     Genre("Sci-Fi"): 1}
#
#
# def test_top_actors(stats1):
#     movie2 = Movie('Brin', 2002)
#     movie2.add_actor(Actor("Tom Cruise"))
#     stats.user.watch_movie(movie2)
#     stats.update_watched_lists()
#     assert stats.top_actors(2) == [Actor("Tom Cruise"), Actor("Will Smith")]
#     assert stats.top_actors(6) == []
#     assert stats.top_actors(-1) == [Actor("Tom Cruise"), Actor("Will Smith"), Actor("Selena Gomez"),
#                                     Actor("Daniel Radcliff")]
#
#
# def test_top_directors(stats1):
#     assert stats.top_directors(1) == [Director("Peter Jackson")]
#     assert stats.top_directors(6) == []
#     assert stats.top_directors(-1) == [Director("Peter Jackson"), Director("Taika Waititi")]
#
#
# def test_top_genres(stats1):
#     assert stats.top_genres(2) == [Genre("Comedy"), Genre("Action")]
#     assert stats.top_genres(6) == []
#     assert stats.top_genres(-1) == [Genre("Comedy"), Genre("Action"), Genre("Romance"),
#                                     Genre("Drama")]
#
#
# def test_eq():
#     user = User("aram", "one1")
#     movie = Movie('Up', 2009)
#     movie1 = Movie('Down', 2013)
#     movie2 = Movie('Boom', 1999)
#     user.watch_movie(movie)
#     user.watch_movie(movie1)
#     user.watch_movie(movie2)
#     assert stats == Stats(user)
#     print(stats)
#
#
# def test_recs(stats):
#     stat1 = stat_class()
#     print("?D", stat1.watched_movies)
#     filename = '../../data/test.csv'
#     movie_file_reader = MovieFileCSVReader(filename)
#     movie_file_reader.read_csv_file()
#     print("HI", stats.watched_genres)
#     assert stats.make_recommendations(movie_file_reader.dataset_of_movies, -1) == [
#         Movie("Guardians of the Galaxy", 2014), Movie("Split", 2016), Movie("Sing", 2016), Movie("Suicide Squad", 2016)]

from AditiFlix_App.domainmodel.movie import Movie
from AditiFlix_App.domainmodel.director import Director
from AditiFlix_App.domainmodel.genre import Genre
from AditiFlix_App.domainmodel.actor import Actor
from AditiFlix_App.domainmodel.user import User
from AditiFlix_App.domainmodel.stats import Stats
from AditiFlix_App.adapters.datafilereaders.movie_file_csv_reader import MovieFileCSVReader

import pytest

@pytest.fixture
def user():
    movie = Movie('Up', 2009)
    movie.add_actor(Actor("Will Smith"))
    movie.add_actor(Actor("Daniel Radcliff"))
    movie.add_genre(Genre("Comedy"))
    movie.add_genre(Genre("Drama"))
    director = Director("Peter Jackson")
    movie.director = director

    movie1 = Movie('Down', 2013)
    movie1.add_actor(Actor("Tom Cruise"))
    movie1.add_actor(Actor("Selena Gomez"))
    movie1.add_genre(Genre("Comedy"))
    movie1.add_genre(Genre("Romance"))
    director = Director("Peter Jackson")
    movie1.director = director

    movie2 = Movie('Boom', 1999)
    movie2.add_actor(Actor("Will Smith"))
    movie2.add_actor(Actor("Tom Cruise"))
    movie2.add_genre(Genre("Comedy"))
    movie2.add_genre(Genre("Action"))
    director = Director("Taika Waititi")
    movie2.director = director

    user = User("aram", "one1")
    user.watch_movie(movie)
    user.watch_movie(movie1)
    user.watch_movie(movie2)
    return user


@pytest.fixture
def stats(user):
    stats = Stats(user)
    return stats

def test_init(stats):
    assert stats.user == User("aram", "one1", [], [], None, 0)
    assert stats.watched_movies == [Movie("Up", 2009), Movie("Down", 2013), Movie("Boom", 1999)]
    assert stats.watched_actors == {Actor("Will Smith"): 2, Actor("Daniel Radcliff"): 1, Actor("Selena Gomez"): 1,
                                    Actor("Tom Cruise"): 2}
    assert stats.watched_directors == {Director("Peter Jackson"): 2, Director("Taika Waititi"): 1}
    assert stats.watched_genres == {Genre("Comedy"): 3, Genre("Romance"): 1, Genre("Drama"): 1, Genre("Action"): 1}


def test_update(stats):
    movie2 = Movie('Brain', 2002)
    movie2.add_actor(Actor("Julia Roberts"))
    movie2.add_actor(Actor("Tom Cruise"))
    movie2.add_genre(Genre("Sci-Fi"))
    movie2.add_genre(Genre("Action"))
    director = Director("Christopher Nolan")
    movie2.director = director

    stats.user.watch_movie(movie2)
    stats.update_watched_lists()

    assert stats.user == User("aram", "one1", [], [], 0)
    assert stats.watched_movies == [Movie("Up", 2009), Movie("Down", 2013), Movie("Boom", 1999), Movie("Brain", 2002)]
    assert stats.watched_actors == {Actor("Will Smith"): 2, Actor("Daniel Radcliff"): 1, Actor("Selena Gomez"): 1,
                                    Actor("Tom Cruise"): 3, Actor("Julia Roberts"): 1}
    assert stats.watched_directors == {Director("Peter Jackson"): 2, Director("Taika Waititi"): 1,
                                       Director("Christopher Nolan"): 1}
    assert stats.watched_genres == {Genre("Comedy"): 3, Genre("Romance"): 1, Genre("Drama"): 1, Genre("Action"): 2,
                                    Genre("Sci-Fi"): 1}

def test_top_actors(stats):
    movie2 = Movie('Brin', 2002)
    movie2.add_actor(Actor("Tom Cruise"))
    stats.user.watch_movie(movie2)
    stats.update_watched_lists()
    assert stats.top_actors(2) == [Actor("Tom Cruise"), Actor("Will Smith")]
    assert stats.top_actors(6) == []
    assert stats.top_actors(-1) == [Actor("Tom Cruise"), Actor("Will Smith"), Actor("Selena Gomez"),
                                    Actor("Daniel Radcliff")]


def test_top_directors(stats):
    assert stats.top_directors(1) == [Director("Peter Jackson")]
    assert stats.top_directors(6) == []
    assert stats.top_directors(-1) == [Director("Peter Jackson"), Director("Taika Waititi")]


def test_top_genres(stats):
    assert stats.top_genres(2) == [Genre("Comedy"), Genre("Action")]
    assert stats.top_genres(6) == []
    assert stats.top_genres(-1) == [Genre("Comedy"), Genre("Action"), Genre("Romance"),
                                    Genre("Drama")]


# def test_recs(stats):
#     filename = '../../data/test.csv'
#     movie_file_reader = MovieFileCSVReader(filename)
#     movie_file_reader.read_csv_file()
#     assert stats.make_recommendations(movie_file_reader.dataset_of_movies, -1) == [
#         Movie("Guardians of the Galaxy", 2014), Movie("Split", 2016), Movie("Sing", 2016), Movie("Suicide Squad", 2016)]
