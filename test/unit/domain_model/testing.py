from datetime import datetime

class Genre:

    def __init__(self, genre_name: str):
        if genre_name == "" or type(genre_name) is not str:
            self.__genre_name = None
        else:
            self.__genre_name = genre_name.strip()

    @property
    def genre_name(self) -> str:
        return self.__genre_name

    def __repr__(self):
        return f"<Genre {self.__genre_name}>"

    def __eq__(self, other):
        if not isinstance(other, Genre):
            return False
        return other.__genre_name == self.__genre_name

    def __lt__(self, other):
        if self.__genre_name < other.__genre_name:
            return True
        return False

    def __le__(self, other):
        if self.__genre_name <= other.__genre_name:
            return True
        return False

    def __hash__(self):
        return hash((self.__genre_name,))


class Actor:

    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()

        self.__actor_colleague_list = list()

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    @property
    def actor_colleague_list(self) -> str:
        return self.__actor_colleague_list
        #return iter(self.__actor_colleague_list)

    def get_next_colleague(self):
        return iter(self.__actor_colleague_list)

    @actor_colleague_list.setter
    def actor_colleague_list(self, new_list):  # Only adds in legitimate actors. Completely replaces the original
        self.__actor_colleague_list = list()
        if type(new_list) == list:
            for element in new_list:
                if not isinstance(element, Actor):
                    raise ValueError
                    return -1
                elif element.actor_full_name is not None:
                    self.__actor_colleague_list.append(element)
        return 1

    def add_actor_colleague(self, colleague: 'Actor'):
        if not isinstance(colleague, Actor):
            return -1
        elif self.check_if_this_actor_worked_with(colleague):
            return 0
        elif colleague.actor_full_name is None:
            return 0
        else:
            self.__actor_colleague_list.append(colleague)
        return 1

    def check_if_this_actor_worked_with(self, colleague: 'Actor'):
        if colleague in self.__actor_colleague_list:
            return True
        else:
            return False

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        if not isinstance(other, Actor):
            return False
        return other.actor_full_name == self.__actor_full_name

    def __lt__(self, other):
        if self.__actor_full_name < other.actor_full_name:
            return True
        return False

    def __hash__(self):
        return hash((self.actor_full_name,))


class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        if not isinstance(other, Director):
            return False
        return other.director_full_name == self.__director_full_name

    def __lt__(self, other):
        if self.__director_full_name < other.director_full_name:
            return True
        return False

    def __hash__(self):
        return hash((self.director_full_name,))






class Movie:

    def __init__(self, movie_title: str, movie_release_year: int):
        if movie_title == "" or type(movie_title) is not str:
            self.__title = None
        else:
            self.__title = movie_title.strip()

        if type(movie_release_year) is not int or movie_release_year < 1990 or movie_release_year > datetime.now().year:
            self.__release_year = None
        else:
            self.__release_year = movie_release_year

        self.__description = None
        self.__director = None
        self.__actors = list()
        self.__genres = list()
        self.__runtime_minutes = None

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
        if type(movie_release_year) is not int or movie_release_year < 1990 or movie_release_year > datetime.now().year:
            self.__release_year = None
        else:
            self.__release_year = movie_release_year

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
        #return iter(self.__actors)

    def get_next_actor(self):
        return iter(self.__actors)

    def add_actor(self, actor):
        if isinstance(actor, Actor):
            if actor.actor_full_name is not None:
                if actor not in self.__actors:
                    self.__actors.append(actor)

    def remove_actor(self, actor):
        for i in range(len(self.__actors)-1, -1, -1):
            if actor == self.__actors[i]:
                self.__actors.pop(i)


    @property
    def genres(self):
        return self.__genres
        #return iter(self.__genres)

    def get_next_genre(self):
        return iter(self.__genres)

    def add_genre(self, genre):
        if isinstance(genre, Genre):
            if genre.genre_name is not None:
                if genre not in self.__genres:
                    self.__genres.append(genre)

    def remove_genre(self, genre):
        for i in range(len(self.__genres)-1, -1, -1):
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

    def __repr__(self):
        return f"<Movie {self.title}, {self.release_year}>"

    def __eq__(self, other):
        if not isinstance(other, Movie):
            return False
        return other.title == self.__title and other.release_year == self.__release_year

    def __lt__(self, other):
        if self.__title is None or other.title is None:
            return
        if self.__title < other.title:
            return True
        elif self.__title == other.title:
            if self.__release_year < other.release_year:
                return True
        return False

    def __hash__(self):
        return hash((self.__title, self.__release_year))

class Review:

    def __init__(self, movie, review_text, rating):
        if type(rating) is not int or rating < 1 or rating > 10:
            self.__rating = None
        else:
            self.__rating = rating

        if not isinstance(movie, Movie):
            self.__movie = None
        else:
            self.__movie = movie

        if type(review_text) is not str or review_text == "":
            self.__review_text = None
        else:
            self.__review_text = review_text

        self.__timestamp: datetime = datetime.today()

    @property
    def rating(self):
        return self.__rating

    @property
    def movie(self):
        return self.__movie

    @property
    def review_text(self):
        return self.__review_text

    @property
    def timestamp(self):
        return self.__timestamp

    def __repr__(self):
        return f"<Rating {self.__rating}, Review {self.__review_text}>"

    def __eq__(self, other):
        if not isinstance(other, Review):
            return False
        return other.review_text == self.__review_text \
            and other.rating == self.__rating \
            and other.movie == self.__movie \
            and other.timestamp == self.__timestamp

class User:

    def __init__(self, username, password):
        if type(username) is not str or username == "":
            self.__username = None
        else:
            self.__username = username.strip().lower()

        if type(password) is not str or password == "":
            self.__password = None
        else:
            self.__password = password

        self.__watched_movies = list()
        self.__reviews = list()
        self.__time_spent_watching_movies_minutes = 0

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
            self.__watched_movies.append(movie)
            if movie.runtime_minutes is not None:
                self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if isinstance(review, Review):
            self.__reviews.append(review)


