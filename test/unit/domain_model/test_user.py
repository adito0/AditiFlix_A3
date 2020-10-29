from AditiFlix_App.domainmodel.review import Review
from AditiFlix_App.domainmodel.movie import Movie
from AditiFlix_App.domainmodel.user import User
from AditiFlix_App.domainmodel.movielist import MovieList

import pytest


@pytest.fixture
def user():
    return User("     ARAM485  ", "Spiderman209", )

def test_init(user):
    assert user.watched_movies == MovieList()
    assert user.time_spent_watching_movies_minutes == 0
    assert user.reviews == []
    assert user.username == "aram485"
    assert user.password == "Spiderman209"
    user1 = User("", 4)
    user2 = User(45, "")
    assert user1.username is None
    assert user1.password is None
    assert user2.username is None
    assert user2.password is None

    mov = Movie("Up", 2009)
    mov2 = Movie("Down", 2019)
    mov.runtime_minutes = 200
    mov2.runtime_minutes = 160
    review = Review(mov, "Nice", 6)
    time = mov.runtime_minutes + mov2.runtime_minutes
    watched_already = MovieList()
    watched_already.add_movie(mov)
    watched_already.add_movie(mov2)
    user2 = User("     ARAM85  ", "spideran", watched_already, None , (review,), time)

    print("user2:", user2)
    print(user2.watched_movies.list)
    assert user2.watched_movies.list == (Movie("Up", 2009), Movie("Down", 2019))
    assert user2.time_spent_watching_movies_minutes == 360
    assert user2.username == "aram85"
    assert user2.password == "spideran"


def test_compare():
    user1 = User("Brad Pitt", 4)
    user2 = User("brad PiTt", 5)
    assert user1 == user2
    user2 = 4
    assert user1 != user2
    user1 = User("", "goat")
    user2 = User(45, "HFTbhy")
    assert user1 == user2


def test_lt():
    user1 = User("Brad Pitt", 4)
    user2 = User("brae Pitt", 7)
    assert user1 < user2


def test_hash():
    user1 = User("Brad Pitt", "goat")
    user2 = User("Brad Pitt", "goat")
    assert hash(user1) == hash(user2)
    user2 = User("Taika Waititj","goat")
    assert hash(user1) != hash(user2)
    dict1 = dict()
    dict1[user1] = user2
    assert dict1[user1] == user2
    assert repr(dict1[user1]) == "<User taika waititj>"
    user1 = User("", "friends")
    user2 = User(9, 6)
    dict1[user1] = user2
    assert dict1[user1] == user2
    assert repr(dict1[user1]) == "<User None>"

def test_watch_movie(user):
    user.watch_movie(3)
    assert user.watched_movies == MovieList()
    assert user.time_spent_watching_movies_minutes == 0
    mov = Movie("Up", 2009)
    user.watch_movie(mov)
    assert user.watched_movies.list == (Movie("Up", 2009),)
    assert user.time_spent_watching_movies_minutes == 0
    mov.runtime_minutes = 123
    user.watch_movie(mov)
    assert user.watched_movies.list == (Movie("Up", 2009),)
    assert user.time_spent_watching_movies_minutes == 123
    user.watch_movie(mov)
    assert user.watched_movies.list == (Movie("Up", 2009),)
    assert user.time_spent_watching_movies_minutes == 246

def test_add_review(user):
    assert user.reviews == []
    mov = Movie("Up", 2009)
    review = Review(mov, "Nice", 6)
    user.add_review(review)
    assert user.reviews == [Review(mov, "Nice", 6)]
    user.add_review(4)
    assert user.reviews == [Review(mov, "Nice", 6)]
    review = Review(mov, "Okay", 4)
    user.add_review(review)
    assert user.reviews == [Review(mov, "Nice", 6), Review(mov, "Okay", 4)]

