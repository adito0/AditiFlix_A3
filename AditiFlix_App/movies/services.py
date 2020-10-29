

import random
from AditiFlix_App.adapters.movie_repository import AbstractRepository


from AditiFlix_App.domainmodel.movie import Movie
from AditiFlix_App.auth.services import UnknownUserException


def get_random_movies(number, repo: AbstractRepository):
    random_ids = random.sample(range(0, repo.get_number_of_movies()-1), number)
    list_of_movies = []
    for id in random_ids:
        list_of_movies.append(repo.get_movies()[id])
    return list_of_movies

def get_movie(name:str, year:int, repo: AbstractRepository):
    return repo.get_movie(name, year)

def get_ordered_movies_for_year(start_index,number, year, repo: AbstractRepository):
    list_of_movies = []
    return repo.get_movies_for_year(year)[start_index:start_index+number]

def get_number_movies_for_year(year, repo: AbstractRepository):
    return len(repo.get_movies_for_year(year))

def search_for_movies(search, repo: AbstractRepository):
    # First parameter is genre then actor then director e.g Family&Will+Smith&Taika+Waititi
    list_params = search.split("@")
    for i in range(len(list_params)):
        list_params[i] = list_params[i].replace("+", " ")
    print(search, list_params)
    dict_movies = dict()
    dict_movies['Genres'] = []
    dict_movies['Actors'] = []
    dict_movies['Directors'] = []
    final_list = []
    if list_params[0] != "":
        list_genres = list_params[0].split(";")
        list_movies = repo.get_movies_for_genre(list_genres[0])
        for movie in list_movies:
            flag = True
            for genre in list_genres:
                if movie not in repo.get_movies_for_genre(genre):
                    flag = False
            if flag:
                dict_movies['Genres'].append(movie)
    else:
        dict_movies['Genres'] = repo.get_movies()
    if list_params[1] != "":
        list_actors = list_params[1].split(";")
        list_movies = repo.get_movies_for_actor(list_actors[0])
        for movie in list_movies:
            flag = True
            for actor in list_actors:
                if movie not in repo.get_movies_for_actor(actor):
                    flag = False
            if flag:
                dict_movies['Actors'].append(movie)
    else:
        dict_movies['Actors'] = repo.get_movies()
    if list_params[2] != "":
        list_dir = list_params[2].split(";")
        list_movies = repo.get_movies_for_director(list_dir[0])
        for movie in list_movies:
            flag = True
            for dir in list_dir:
                if movie not in repo.get_movies_for_director(dir):
                    flag = False
            if flag:
                dict_movies['Directors'].append(movie)
    else:
        dict_movies['Directors'] = repo.get_movies()
    for movie in dict_movies['Genres']:
        if movie in dict_movies['Actors'] and movie in dict_movies['Directors']:
            final_list.append(movie)

    print("Final", final_list)
    return final_list

def get_reviews(movie:Movie,repo: AbstractRepository):
    return repo.get_reviews_for_movie(movie)

def get_user(username: str, repo: AbstractRepository):
    user = repo.get_user(username)
    if user is None:
        raise UnknownUserException
    return user