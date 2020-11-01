from AditiFlix_App.domainmodel.movie import Movie
from AditiFlix_App.domainmodel.review import Review
from AditiFlix_App.domainmodel.movielist import MovieList


class User:

    def __init__(self, username, password, watched=tuple(), watchlist=tuple(), reviews=tuple(), time_spent=0):
        if type(username) is not str or username == "":
            self.__username = None
        else:
            self.__username = username.strip().lower()

        if type(password) is not str or password == "":
            self.__password = None
        else:
            self.__password = password
        if not isinstance(watched, MovieList):
            self.__watched_movies = MovieList()
        else:
            self.__watched_movies = watched
        if isinstance(reviews, tuple):
            self.__reviews = list(reviews)
        else:
            self.__reviews = []

        if type(time_spent) is float or type(time_spent) is int:
            self.__time_spent_watching_movies_minutes = time_spent
        else:
            self.__time_spent_watching_movies_minutes = 0

        if not isinstance(watchlist, MovieList):
            self.__watchlist = MovieList()
        else:
            self.__watchlist = watchlist

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def watched_movies(self):
        return self.__watched_movies

    @property
    def watchlist(self):
        return self.__watchlist

    @property
    def reviews(self):
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent_watching_movies_minutes

    def __repr__(self):
        return f"<User {self.__username}>"

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return other.username == self.__username

    def __lt__(self, other):
        if self.__username < other.username:
            return True
        return False

    def __hash__(self):
        return hash((self.username,))

    def watch_movie(self, movie):
        if isinstance(movie, Movie):
            self.__watched_movies.add_movie(movie)
            if movie in self.__watchlist:
                self.__watchlist.remove_movie(movie)
            if movie.runtime_minutes is not None:
                self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def watchlist_movie(self, movie):
        if isinstance(movie, Movie):
            self.__watchlist.add_movie(movie)

    def remove_movie(self, movie):
        if isinstance(movie, Movie):
            self.__watchlist.remove_movie(movie)

    def add_review(self, review):
        if isinstance(review, Review):
            self.__reviews.append(review)
