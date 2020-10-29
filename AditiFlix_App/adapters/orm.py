from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date, DateTime, Float, VARCHAR, NVARCHAR,
    ForeignKey
)

from sqlalchemy.orm import mapper, relationship

from AditiFlix_App.domainmodel.user import User
from AditiFlix_App.domainmodel.actor import Actor
from AditiFlix_App.domainmodel.director import Director
from AditiFlix_App.domainmodel.movie import Movie
from AditiFlix_App.domainmodel.review import Review
from AditiFlix_App.domainmodel.genre import Genre

metadata = MetaData()

users = Table(
    'users', metadata,
    Column('user_id', Integer, primary_key=True, autoincrement=True),
    Column('username', String(255), unique=True, nullable=False),
    Column('password', String(255), nullable=False),
    Column('time_spent_watching_movies', Integer, nullable=False)
)

movies = Table(
    'movies', metadata,
    Column('movie_id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(1024), nullable=False),
    Column('release_year', String(1024), primary_key=True, nullable=False),
    Column('runtime_minutes', Integer, nullable=True),
    Column('description', String(1024), nullable=True),
    Column('votes', Integer, nullable=True),
    Column('rating', Float(), nullable=True),
    Column('image', String(1024), nullable=True)
)

actors = Table(
    'actors', metadata,
    Column('actor_id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(1024), unique=True, nullable=False),
    Column('movie_id', ForeignKey('movies.movie_id')),
)

directors = Table(
    'directors', metadata,
    Column('director_id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(1024), unique=True, nullable=False),
    Column('movie_id', ForeignKey('movies.movie_id')),
)

genres = Table(
    'genres', metadata,
    Column('genre_id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(1024), unique=True, nullable=False),
    Column('movie_id', ForeignKey('movies.movie_id')),
)

reviews = Table(
    'reviews', metadata,
    Column('review_id', Integer, primary_key=True, autoincrement=True),
    Column('text', String(1024), nullable=False),
    Column('rating', Integer, nullable=False),
    Column('time', DateTime, nullable=False),
    Column('movie_id', ForeignKey('movies.movie_id'))
)


def map_model_to_tables():
    mapper(User, users, properties={
        '__username': users.c.username,
        '__password': users.c.password,
        '__time_spent_watching_movies_minutes': users.c.time_spent_watching_movies
    })

    mapper(Movie, movies, properties={
        '__title': movies.c.title,
        '__description': movies.c.description,
        '__release_year': movies.c.release_year,
        '__runtime_minutes': movies.c.runtime_minutes,
        '__rating': movies.c.rating,
        '__votes': movies.c.votes,
        '__image': movies.c.image
    })

    mapper(Actor, actors, properties={
        '__actor_full_name': actors.c.name,
    })

    mapper(Director, directors, properties={
        '__director_full_name': directors.c.name
    })

    mapper(Genre, genres, properties={
        '__genre_name': genres.c.name
    })

    mapper(Review, reviews, properties={
        '__rating': reviews.c.rating,
        '__review_text': reviews.c.text,
        '__timestamp': reviews.c.time
    })
