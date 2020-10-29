from AditiFlix_App.domainmodel.movie import Movie
from AditiFlix_App.domainmodel.review import Review
from AditiFlix_App.auth.services import UnknownUserException
from AditiFlix_App.adapters.movie_repository import AbstractRepository


def get_reviews(movie: Movie, repo: AbstractRepository):
    return repo.get_reviews_for_movie(movie)


def write_review(title, year, text, rating, username, repo: AbstractRepository):
    user = get_user(username, repo)
    movie_reviewed = repo.get_movie(title, year)
    review = Review(movie_reviewed, text, rating)
    repo.add_review(review)
    user.add_review(review)


def get_user(username: str, repo: AbstractRepository):
    user = repo.get_user(username)
    if user is None:
        raise UnknownUserException
    return user


def get_movie(name: str, year: int, repo: AbstractRepository):
    return repo.get_movie(name, year)
