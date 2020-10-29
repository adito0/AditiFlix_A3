import csv
import os
from datetime import date, datetime
from typing import List
import json

from pip._vendor import requests

from bisect import bisect, bisect_left, insort_left

from werkzeug.security import generate_password_hash

from AditiFlix_App.adapters.movie_repository import AbstractRepository, RepositoryException
from AditiFlix_App.domainmodel.movie import Movie
from AditiFlix_App.domainmodel.user import User
from AditiFlix_App.domainmodel.actor import Actor
from AditiFlix_App.domainmodel.director import Director
from AditiFlix_App.domainmodel.genre import Genre
from AditiFlix_App.domainmodel.review import Review
from AditiFlix_App.domainmodel.stats import Stats
from AditiFlix_App.domainmodel.watching_simulation import WatchingSimulation
from AditiFlix_App.domainmodel.movielist import MovieList


class MemoryRepository(AbstractRepository):
    # Articles ordered by date, not id. id is assumed unique.

    def __init__(self):
        self.__dataset_of_movies = list()
        self.__dataset_of_actors = list()
        self.__dataset_of_genres = list()
        self.__dataset_of_directors = list()
        self.__dataset_of_users = list()
        self.__dataset_of_reviews = list()

    def add_user(self, user: User):
        self.__dataset_of_users.append(user)

    def get_user(self, username) -> User:
        for user in self.__dataset_of_users:
            if user.username == username:
                return user
        return None
        # return next((user for user in self.__dataset_of_users if user.username == username), None)

    def get_users(self):
        return self.__dataset_of_users

    def add_review(self, review: Review):
        self.__dataset_of_reviews.append(review)

    def get_reviews_for_movie(self, movie: Movie):
        review_list = []
        for review in self.__dataset_of_reviews:
            if review.movie == movie:
                review_list.append(review)
        return review_list

    def get_reviews(self):
        return self.__dataset_of_reviews

    def add_movie(self, movie: Movie):
        if movie not in self.__dataset_of_movies:
            insort_left(self.__dataset_of_movies, movie)

    def get_movies(self):
        return self.__dataset_of_movies

    def get_movie(self, title: str, year: int) -> Movie:
        list_of_movies = self.get_movies_by_title(title)
        for movie in list_of_movies:
            if year == movie.release_year:
                return movie
        return None

    def get_movies_by_title(self, title: str) -> List[Movie]:
        list_of_movies = []
        for movie in self.__dataset_of_movies:
            if title == movie.title:
                list_of_movies.append(movie)
        return list_of_movies

    def get_movies_for_year(self, year: int) -> List[Movie]:
        list_of_movies = []
        for movie in self.__dataset_of_movies:
            if year == movie.release_year:
                list_of_movies.append(movie)
        return list_of_movies

    def get_number_of_movies(self):
        return len(self.__dataset_of_movies)

    def get_movies_for_genre(self, genre_name: str):
        list_of_movies = []
        for movie in self.__dataset_of_movies:
            if not len(movie.genres) == 0:
                if Genre(genre_name) in movie.genres:
                    list_of_movies.append(movie)
        return list_of_movies

    def get_movies_for_director(self, director_name: str):
        list_of_movies = []
        for movie in self.__dataset_of_movies:
            if movie.director is not None:
                if director_name == movie.director.director_full_name:
                    list_of_movies.append(movie)
        return list_of_movies

    def get_movies_for_actor(self, actor_name: str):
        list_of_movies = []
        for movie in self.__dataset_of_movies:
            if not len(movie.actors) == 0:
                if Actor(actor_name) in movie.actors:
                    list_of_movies.append(movie)
        return list_of_movies

    def add_genre(self, genre: Genre):
        if genre not in self.__dataset_of_genres:
            insort_left(self.__dataset_of_genres, genre)

    def get_genres(self) -> List[Genre]:
        return self.__dataset_of_genres

    def add_actor(self, actor):
        if actor not in self.__dataset_of_actors:
            insort_left(self.__dataset_of_actors, actor)

    def get_actors(self):
        return self.__dataset_of_actors

    def add_director(self, director: Director):
        if director not in self.__dataset_of_directors:
            insort_left(self.__dataset_of_directors, director)

    def get_directors(self):
        return self.__dataset_of_directors


def read_csv_file(filename: str):
    with open(filename, mode='r', encoding='utf-8-sig') as infile:
        reader = csv.DictReader(infile)

        # Read remaining rows from the CSV file.
        for row in reader:
            yield row


def load_movies(data_path: str, repo: MemoryRepository, data_file):
    print("DATA: ", data_file)
    for row in read_csv_file(os.path.join(data_path, data_file)):
        try:
            movie = Movie(row['Title'], int(row['Year']))
        except ValueError:
            print("Invalid release year")
        else:
            director = Director(row['Director'].strip())
            actors = row['Actors'].split(",")
            genres = row['Genre'].split(",")
            movie.director = director
            repo.add_director(director)
            movie.description = row['Description'].strip()
            for actor_name in actors:
                actor_name = actor_name.strip()
                actor = Actor(actor_name)
                if actor in repo.get_actors():
                    i = repo.get_actors().index(actor)
                    actor = repo.get_actors()[i]
                else:
                    repo.add_actor(actor)
                for actor1_name in actors:
                    actor1_name = actor1_name.strip()
                    if not actor.check_if_this_actor_worked_with(Actor(actor1_name)) and (actor_name != actor1_name):
                        actor.add_actor_colleague(Actor(actor1_name))
                movie.add_actor(actor)
            for genre_name in genres:
                genre = Genre(genre_name.strip())
                movie.add_genre(genre)
                if genre not in repo.get_genres():
                    repo.add_genre(genre)
            try:
                movie.runtime_minutes = int(row['Runtime (Minutes)'])
            except ValueError:
                movie.runtime_minutes = None
            try:
                movie.votes = int(row['Votes'])
            except ValueError:
                movie.votes = None
            try:
                movie.rating = float(row['Rating'])
            except ValueError:
                movie.rating = None
            if movie not in repo.get_movies():
                movie.image = get_image(movie)
                if movie.image == "":
                    movie.image = "../static/none.jpg"
                repo.add_movie(movie)


def load_users(data_path: str, repo: MemoryRepository):
    #    for row in read_csv_file(os.path.join(data_path, 'test1user.csv')):
    print("OS", os.path.join(data_path, 'Data5Users.csv'))
    for row in read_csv_file(os.path.join(data_path, 'Data5Users.csv')):
        watching_time = 0
        watchlist_string = row['Watchlist'].strip().split("|")
        watchlist = MovieList()
        for movie_name in watchlist_string:
            movie_name = movie_name.strip().split(";")
            try:
                movie = Movie(movie_name[0].strip(), int(movie_name[1].strip()))
            except:
                print("Invalid movie")
            else:
                if movie in repo.get_movies():
                    i = repo.get_movies().index(movie)
                    movie = repo.get_movies()[i]
                else:
                    pass
                    # repo.add_movie(movie)
                if movie not in watchlist.list:
                    watchlist.add_movie(movie)

        watched_string = row["Watched_movies"].strip().split("|")
        watched = MovieList()
        for movie_name in watched_string:
            movie_name = movie_name.strip().split(";")
            try:
                movie = Movie(movie_name[0].strip(), int(movie_name[1].strip()))
            except:
                print("Invalid movie")
            else:
                if movie in repo.get_movies():
                    i = repo.get_movies().index(movie)
                    movie = repo.get_movies()[i]
                else:
                    pass
                    # repo.add_movie(movie)
                if movie not in watched:
                    watched.add_movie(movie)
                    if movie.runtime_minutes is not None:
                        try:
                            watching_time += movie.runtime_minutes
                        except:
                            pass

        reviews_string = row["Reviews"].strip().split("|")
        review_list = []
        for review_string in reviews_string:
            review_string = review_string.strip().split(";")
            if len(review_string) > 4:
                try:
                    movie = Movie(review_string[0].strip(), int(review_string[1].strip()))
                except:
                    print("Invalid movie")
                else:
                    if movie in repo.get_movies():
                        i = repo.get_movies().index(movie)
                        movie = repo.get_movies()[i]
                    else:
                        pass
                        # repo.add_movie(movie)

                    review_message = review_string[3].strip()

                    try:
                        # timestamp = datetime.strptime(review_string[4].strip())
                        timestamp = datetime.fromisoformat(review_string[4].strip())
                    except:
                        pass
                    else:
                        try:
                            rating = float(review_string[2])
                        except:
                            pass
                        else:
                            review = Review(movie, review_message, rating)
                            review.timestamp = timestamp
                            review_list.append(review)
                            repo.add_review(review)
        user = User(
            username=row['Username'].strip(),
            password=generate_password_hash(row['Password'].strip()),
            watched=watched,
            reviews=tuple(review_list),
            time_spent=watching_time,
            watchlist=watchlist
        )
        repo.add_user(user)


def populate(data_path: str, repo: MemoryRepository, data_file):
    # Load articles and tags into the repository.
    load_movies(data_path, repo, data_file)

    # Load users into the repository.
    load_users(data_path, repo)


def get_image(movie: Movie = Movie("Split", 2016)):
    token = "adea3d0d"
    token = "40e73228"
    movie_name = movie.title.replace(" ", "+")
    movie_year = movie.release_year
    url = "http://www.omdbapi.com/?apikey=" + token + "&t=" + movie_name.lower() + "&y=" + str(movie_year)
    r = requests.get(url).json()
    if r['Response'] == "True":
        return r['Poster']


def test_populate():
    # Can only use with test.csv and Data5Users.csv
    TEST_DATA_PATH = os.path.join('C:', os.sep, 'Users', 'aditi', 'Documents', 'COMPSCI235', 'AFlix_A2', 'AFLix_A2',
                                  'test', 'data')
    repo = MemoryRepository()
    populate(TEST_DATA_PATH, repo, 'Data13Movies.csv')
    repo.get_movies()
    assert repr(
        repo.get_actors()) == "[<Actor Anya Taylor-Joy>, <Actor Bradley Cooper>, <Actor Charlize Theron>, <Actor Chris Pratt>, <Actor Haley Lu Richardson>, <Actor Jared Leto>, <Actor Jessica Sula>, <Actor Logan Marshall-Green>, <Actor Margot Robbie>, <Actor Matthew McConaughey>, <Actor Michael Fassbender>, <Actor Noomi Rapace>, <Actor Reese Witherspoon>, <Actor Scarlett Johansson>, <Actor Seth MacFarlane>, <Actor Vin Diesel>, <Actor Viola Davis>, <Actor Will Smith>, <Actor Zoe Saldana>]"
    assert repr(
        repo.get_directors()) == "[<Director David Ayer>, <Director James Gunn>, <Director M. Night Shyamalan>, <Director Ridley Scott>, <Director Taika Waititi>]"
    assert repr(
        repo.get_genres()) == "[<Genre Action>, <Genre Adventure>, <Genre Animation>, <Genre Family>, <Genre Fantasy>, <Genre Horror>, <Genre Mystery>, <Genre Sci-Fi>, <Genre Thriller>]"
    assert repr(
        repo.get_users()) == "[<User aram485>, <User doggirl>, <User deedee>, <User markrulesworld>, <User noname>]"
    assert repr(
        repo.get_reviews()) == "[<Rating 9.0, Review I love this movie so much!! It really makes you think>, <Rating 8.0, Review This one is great for the kids with a good laugh and what not>, <Rating 5.0, Review This movie was alright. I couldn't even finish it because it was so boring>, <Rating 10.0, Review Wow!>]"
    assert repr(
        repo.get_movies()) == "[<Movie Guardians of the Galaxy, 2014>, <Movie Lion, 2019>, <Movie Prometheus, 2012>, <Movie Sing, 2016>, <Movie Split, 2016>, <Movie Suicide Squad, 2016>]"
