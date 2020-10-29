import os
import pytest

from AditiFlix_App import create_app
from AditiFlix_App.adapters import memory_repository
from AditiFlix_App.adapters.memory_repository import MemoryRepository
#
# TEST_DATA_PATH = os.path.join('C:', os.sep, 'Users', 'aditi', 'Documents', 'COMPSCI235', 'AFlix_A2', 'AFLix_A2',
#                              'AditiFLix_App', 'adapters', 'datafiles')

TEST_DATA_PATH = os.path.join('C:', os.sep, 'Users', 'aditi', 'Documents', 'COMPSCI235', 'AFlix_A2', 'AFLix_A2',
                              'test', 'data')


@pytest.fixture
def in_memory_repo():
    repo = MemoryRepository()
    memory_repository.populate(TEST_DATA_PATH, repo, 'Data13Movies.csv')
    return repo


@pytest.fixture
def client():
    my_app = create_app({
        'TESTING': True,                                # Set to True during testing.
        'TEST_DATA_PATH': TEST_DATA_PATH,               # Path for loading test data into the repository.
        'WTF_CSRF_ENABLED': False,                       # test_client will not send a CSRF token, so disable validation.
        'RECAPTCHA_DISABLE' : True
    })

    return my_app.test_client()


class AuthenticationManager:
    def __init__(self, client):
        self._client = client

    def login(self, username='aram485', password='one1ONE1'):
        return self._client.post(
            'auth/signin',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthenticationManager(client)
