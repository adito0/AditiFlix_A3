from AditiFlix_App.domainmodel.movie import Movie
from datetime import datetime, timedelta


class WatchingSimulation:

    def __init__(self):
        self.__movie: Movie = None
        self.__playing: bool = False
        self.__paused: bool = False
        self.__time_played: int = None
        self.__now: int = None

    def watch_movie(self, movie: Movie):
        if movie.runtime_minutes is None:
            return False
        else:
            self.__movie = movie
            self.__playing = True
            self.__time_played = 0
            self.__paused: bool = False
            self.__now = datetime.now()
            return True

    def check_if_finished(self):
        elapsed: timedelta = datetime.now() - self.__now
        elapsed_time: int = elapsed.total_seconds()
        self.__now = datetime.now()
        if not self.__paused:
            self.__time_played += elapsed_time
        if self.__time_played > self.__movie.runtime_minutes*60:
            self.__movie = None
            self.__playing: bool = False
            self.__paused = False
            self.__time_played: int = None
            self.__now: datetime = None
            return True
        return False

    def pause(self):
        if self.__playing and not self.__paused:
            elapsed: datetime = datetime.now() - self.__now
            elapsed_time: int = elapsed.total_seconds()
            self.__time_played += elapsed_time
            self.__paused = True
            return True
        return False

    def play(self):
        if self.__playing and self.__paused:
            self.__now = datetime.now()
            self.__paused = False
            return True
        return False

    @property
    def movie(self):
        return self.__movie

    @property
    def is_paused(self):
        return self.__paused

    @property
    def time_played(self):
        if self.__playing:
            if self.check_if_finished():
                return self.__movie.runtime_minutes*60
            self.check_if_finished()
            return round(self.__time_played)
        return None

    @property
    def time_left(self):
        if self.__playing:
            if self.check_if_finished():
                return 0
            return round(self.__movie.runtime_minutes*60 - self.__time_played)
        return None

    @property
    def is_playing(self):
        return self.__playing
