from AditiFlix_App.adapters.movie_repository import AbstractRepository
from AditiFlix_App.auth.services import UnknownUserException




def get_user(username: str, repo: AbstractRepository):
    user = repo.get_user(username)
    if user is None:
        raise UnknownUserException
    return user