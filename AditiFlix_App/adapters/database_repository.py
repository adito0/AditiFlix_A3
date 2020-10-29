import csv
import os
from abc import ABC
from typing import List
from sqlalchemy.engine import Engine
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm import scoped_session
from flask import _app_ctx_stack

from AditiFlix_App.adapters.movie_repository import AbstractRepository
from AditiFlix_App.domainmodel.actor import Actor
from AditiFlix_App.domainmodel.director import Director
from AditiFlix_App.domainmodel.genre import Genre
from AditiFlix_App.domainmodel.movie import Movie
from AditiFlix_App.domainmodel.review import Review
from AditiFlix_App.domainmodel.user import User


class SqlAlchemyRepository(AbstractRepository, ABC):

    def __init__(self, session_factory):
        self._session_cm = SessionContextManager(session_factory)

    def close_session(self):
        self._session_cm.close_current_session()

    def reset_session(self):
        self._session_cm.reset_session()

    def add_user(self, user: User):
        with self._session_cm as scm:
            scm.session.add(user)
            scm.commit()

    def get_user(self, username) -> User:
        pass

    def add_review(self, review: Review):
        with self._session_cm as scm:
            scm.session.add(review)
            scm.commit()

    def add_movie(self, movie: Movie):
        with self._session_cm as scm:
            scm.session.add(movie)
            scm.commit()

    def get_movie(self, title: str, year: int) -> Movie:
        movie = None
        try:
            movie = self._session_cm.session.query(Movie).filter(
                Movie.__title == title and Movie.__release_year == year).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass

        return movie

    def get_movies(self):
        movies = self._session_cm.session.query(Movie).all()
        return movies

    def get_movies_by_title(self, title: str) -> Movie:
        pass

    def get_number_of_movies(self):
        number_of_movies = self._session_cm.session.query(Movie).count()
        return number_of_movies

    def get_movies_for_genre(self, genre_name: str):
        if genre_name is None:
            movies = self._session_cm.session.query(Movie).all()
            return movies
        else:
            genres = self._session_cm.session.query(Genre).filter(Genre.__genre_name == genre_name).all()
            print(genres)

    def get_movies_for_director(self, director_name: str):
        pass

    def get_movies_for_actor(self, actor_name: str):
        pass

    def get_reviews_for_movie(movie: Movie):
        pass

    def add_genre(self, genre: Genre):
        with self._session_cm as scm:
            scm.session.add(genre)
            scm.commit()

    def get_genres(self) -> List[Genre]:
        genres = self._session_cm.session.query(Genre).all()
        return genres

    def add_actor(self, actor: Actor):
        with self._session_cm as scm:
            scm.session.add(actor)
            scm.commit()

    def get_actors(self) -> List[Actor]:
        actors = self._session_cm.session.query(Actor).all()
        return actors

    def add_director(self, director: Director):
        with self._session_cm as scm:
            print(director)
            print(director.director_full_name)
            print(director.full_name)
            scm.session.add(director)
            scm.commit()

    def get_directors(self) -> List[Director]:
        pass


def read_csv_file(filename: str):
    with open(filename, mode='r', encoding='utf-8-sig') as infile:
        reader = csv.DictReader(infile)

        # Read remaining rows from the CSV file.
        for row in reader:
            yield row


def get_movies(data_path: str):
    print("DATA: ", data_path)
    movie_records = list()
    for row in read_csv_file(data_path):
        movie_title = row['Title']
        movie_year = row['Year']
        movie_runtime_minutes = int(row['Runtime (Minutes)'])
        movie_description = row['Description'].strip()
        movie_votes = int(row['Votes']) if 'Votes' in row else None
        movie_rating = float(row['Rating']) if 'Rating' in row else None
        movie_records.append(
            (movie_title, movie_year, movie_runtime_minutes, movie_description, movie_votes, movie_rating))
    return movie_records


def get_directors(data_path: str):
    print("DATA: ", data_path)
    director_records = list()
    count = 1
    for row in read_csv_file(data_path):
        director_name = row['Director'].strip()
        director_records.append((director_name, count))
        count += 1
    print(director_records)
    return director_records


def populate(engine: Engine, data_path: str):
    print(data_path)
    conn = engine.raw_connection()
    cursor = conn.cursor()

    movie_records = get_movies(os.path.join(os.getcwd(), "test", "data", data_path))

    insert_movie = (
        "INSERT OR REPLACE INTO movies (title, release_year, runtime_minutes, description, votes, rating)"
        "VALUES (?, ?, ?, ?, ?, ?)"
    )

    cursor.executemany(insert_movie, movie_records)

    print("Movies done!")
    director_records = get_directors(os.path.join(os.getcwd(), "test", "data", data_path))

    insert_director = (
        "INSERT OR REPLACE INTO directors (name, movie_id)"
        "VALUES (?, ?)"
    )

    cursor.executemany(insert_director, director_records)

    conn.commit()
    conn.close()


class SessionContextManager:
    def __init__(self, session_factory):
        self.__session_factory = session_factory
        self.__session = scoped_session(self.__session_factory, scopefunc=_app_ctx_stack.__ident_func__)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @property
    def session(self):
        return self.__session

    def commit(self):
        self.__session.commit()

    def rollback(self):
        self.__session.rollback()

    def reset_session(self):
        # this method can be used e.g. to allow Flask to start a new session for each http request,
        # via the 'before_request' callback
        self.close_current_session()
        self.__session = scoped_session(self.__session_factory, scopefunc=_app_ctx_stack.__ident_func__)

    def close_current_session(self):
        if not self.__session is None:
            self.__session.close()
