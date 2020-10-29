import time

from AditiFlix_App.domainmodel.movie import Movie
from AditiFlix_App.domainmodel.watching_simulation import WatchingSimulation

import pytest


@pytest.fixture
def simulation():
    return WatchingSimulation()


def test_init(simulation):
    assert simulation.movie is None
    assert simulation.is_paused is False
    assert simulation.is_playing is False
    assert simulation.time_left is None
    assert simulation.time_played is None


def test_watch_movie_no_runtime(simulation):
    movie = Movie("Lego", 2019)
    successful = simulation.watch_movie(movie)
    assert successful == False
    assert simulation.movie is None
    assert simulation.is_paused is False
    assert simulation.is_playing is False
    assert simulation.time_left is None
    assert simulation.time_played is None


def test_watch_movie_with_runtime(simulation):
    movie = Movie("Lego", 2019)
    movie.runtime_minutes = 2
    successful = simulation.watch_movie(movie)
    assert successful == True
    assert simulation.movie == Movie("Lego", 2019)
    assert simulation.is_paused is False
    assert simulation.is_playing is True


def test_check_if_finished(simulation): # Takes one minute to run
    movie = Movie("Lego", 2019)
    movie.runtime_minutes = 1
    simulation.watch_movie(movie)
    assert simulation.time_played == 0
    assert simulation.time_left == 60
    time.sleep(2)
    assert simulation.check_if_finished() == False
    assert simulation.time_played == 2
    assert simulation.time_left == 58
    watched = simulation.time_played
    remaining = simulation.time_left
    print()
    while not simulation.check_if_finished():
        assert simulation.time_left == remaining
        assert simulation.time_played == watched
        watched += 1
        remaining -= 1
        print(watched, "\t", remaining)
        time.sleep(1)
    assert simulation.time_played is None
    assert simulation.time_left is None
    assert simulation.is_paused == False
    assert simulation.movie is None
    assert simulation.is_playing is False


def test_pause_play(simulation):
    assert simulation.pause() == False
    movie = Movie("Lego", 2019)
    movie.runtime_minutes = 2
    simulation.watch_movie(movie)
    time.sleep(2)
    simulation.pause()
    time.sleep(2)
    assert simulation.is_paused == True
    simulation.play()
    assert simulation.time_played == 2
    assert simulation.time_left == 118
    assert simulation.is_paused == False
    time.sleep(2)
    assert simulation.time_played == 4
    assert simulation.time_left == 116




