from AditiFlix_App.domainmodel.genre import Genre
from AditiFlix_App.domainmodel.actor import Actor
from AditiFlix_App.domainmodel.director import Director

import datetime


class Movie:

    def __init__(self, movie_title: str, movie_release_year: int):
        if movie_title == "" or type(movie_title) is not str:
            self.__title = None
        else:
            self.__title = movie_title.strip()

        if type(
                movie_release_year) is not int or movie_release_year < 1990 or movie_release_year > datetime.datetime.now().year:
            self.__release_year = None
        else:
            self.__release_year = movie_release_year

        self.__description = None
        self.__director = None  # Done
        self.__actors = list()  # Done
        self.__genres = list()  # Done
        self.__runtime_minutes = None  # Done
        self.__rating = None
        self.__votes = None
        self.__reviews = list()  # Done
        self.__image = ""

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, movie_title):
        if movie_title == "" or type(movie_title) is not str:
            self.__title = None
        else:
            self.__title = movie_title.strip()

    @property
    def release_year(self):
        return self.__release_year

    @release_year.setter
    def release_year(self, movie_release_year):
        if type(
                movie_release_year) is not int or movie_release_year < 1990 or movie_release_year > datetime.datetime.now().year:
            self.__release_year = None
        else:
            self.__release_year = movie_release_year

    # ADD TESTS
    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, image_url: str):
        if isinstance(image_url, str):
            self.__image = image_url

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if type(description) is str and description != "":
            self.__description = description.strip()
        else:
            self.__description = None

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, director):
        # if isinstance(director, Director) and director.director_full_name is not None:
        if isinstance(director, Director):
            self.__director = director
        else:
            self.__director = None

    @property
    def actors(self):
        return self.__actors

    def get_next_actor(self):
        return iter(self.__actors)

    def add_actor(self, actor):
        if isinstance(actor, Actor):
            if actor.actor_full_name is not None:
                if actor not in self.__actors:
                    self.__actors.append(actor)

    def remove_actor(self, actor):
        for i in range(len(self.__actors) - 1, -1, -1):
            if actor == self.__actors[i]:
                self.__actors.pop(i)

    @property
    def genres(self):
        return self.__genres
        # return iter(self.__genres)

    def get_next_genre(self):
        return iter(self.__genres)

    def add_genre(self, genre):
        if isinstance(genre, Genre):
            if genre.genre_name is not None:
                if genre not in self.__genres:
                    self.__genres.append(genre)

    def remove_genre(self, genre):
        for i in range(len(self.__genres) - 1, -1, -1):
            if genre == self.__genres[i]:
                self.__genres.pop(i)

    @property
    def runtime_minutes(self):
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime):
        if type(runtime) is int:
            if runtime < 0:
                raise ValueError
            else:
                self.__runtime_minutes = runtime

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating):
        # Cannot have a rating if votes for the rating are 0 or do not exist
        if self.__votes is None or self.__votes == 0:
            self.__rating = None
        else:
            if type(rating) is float or type(rating) is int:
                if rating < 0 or rating > 10:
                    raise ValueError
                else:
                    self.__rating = rating

    def add_rating(self, new_rating):
        self.__rating = round(((self.__rating * self.__votes) + new_rating) / (self.__votes + 1), 1)
        self.__votes += 1

    @property
    def votes(self):
        return self.__votes

    @votes.setter
    def votes(self, votes):
        if type(votes) is int:
            if votes < 0:
                raise ValueError
            elif votes == 0:
                self.__votes = votes
                self.rating = None
            else:
                self.__votes = votes

    ## NEED TO ADD TESTS
    # @property
    # def reviews(self):
    #     return self.__reviews
    #
    # def add_review(self, review):
    #     if isinstance(review, Review):
    #         self.__reviews.append(review)

    def __repr__(self):
        return f"<Movie {self.title}, {self.release_year}>"

    def __eq__(self, other):
        print(self, other)
        if not isinstance(other, Movie):
            return False
        return other.title == self.title and other.release_year == self.release_year

    def __lt__(self, other):
        if self.__title is None or other.title is None:
            return
        if self.__title < other.title:
            return True
        elif self.__title == other.title:
            print(self.__title, self.__release_year, other.release_year)
            if self.__release_year < other.release_year:
                return True
        return False

    def __hash__(self):
        return hash((self.__title, self.__release_year))
