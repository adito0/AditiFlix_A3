from AditiFlix_App.domainmodel.movie import Movie
from AditiFlix_App.domainmodel.actor import Actor
from AditiFlix_App.domainmodel.genre import Genre
from AditiFlix_App.domainmodel.director import Director

import csv

class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies = list()
        self.__dataset_of_actors = list()
        self.__dataset_of_genres = list()
        self.__dataset_of_directors = list()

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)
            index = 0
            for row in movie_file_reader:
                try:
                    movie = Movie(row['Title'], int(row['Year']))
                except ValueError:
                    print("Invalid release year")
                else:
                    director = Director(row['Director'].strip())
                    actors = row['Actors'].split(",")
                    genres = row['Genre'].split(",")
                    movie.director = director
                    if director not in self.__dataset_of_directors:
                        self.__dataset_of_directors.append(director)
                    movie.description = row['Description'].strip()
                    for actor_name in actors:
                        actor_name = actor_name.strip()
                        actor = Actor(actor_name.strip())
                        if actor in self.dataset_of_actors:
                            i = self.dataset_of_actors.index(actor)
                            actor = self.dataset_of_actors[i]
                        else:
                            self.__dataset_of_actors.append(actor)
                        for actor1_name in actors:
                            actor1_name = actor1_name.strip()
                            if not actor.check_if_this_actor_worked_with(Actor(actor1_name)) and (actor_name != actor1_name):
                                actor.add_actor_colleague(Actor(actor1_name))
                        movie.add_actor(actor)
                    for genre_name in genres:
                        genre = Genre(genre_name.strip())
                        movie.add_genre(genre)
                        if genre not in self.__dataset_of_genres:
                            self.__dataset_of_genres.append(genre)
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
                    if movie not in self.__dataset_of_movies: # Check if this takes into account the same movie but different objects
                        self.__dataset_of_movies.append(movie)
                index += 1

    @property
    def dataset_of_movies(self):
        return self.__dataset_of_movies

    @property
    def dataset_of_actors(self):
        return self.__dataset_of_actors

    @property
    def dataset_of_directors(self):
        return self.__dataset_of_directors

    @property
    def dataset_of_genres(self):
        return self.__dataset_of_genres

