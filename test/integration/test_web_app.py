import pytest

from flask import session


def test_register(client):
    # Check that we retrieve the register page.
    response_code = client.get('/auth/signup').status_code
    assert response_code == 200

    # Check that we can register a user successfully, supplying a valid username and password.
    response = client.post(
        '/auth/signup',
        data={'username': 'fruitninja', 'password': 'twoTWO123','confirmPassword': 'twoTWO123' }
    )
    assert response.headers['Location'] == 'http://localhost/auth/signin'


@pytest.mark.parametrize(('username', 'password', 'cpassword', 'message'), (
        ('', '', '', b'Your username is required'),
        ('cj', '', '', b'Your username is too short'),
        ('test', '', '', b'Please enter a password.'),
        ('test', 'test', '', b'Passwords must match'),
        ('test', 'test', 'test', b'Your password must be at least 8 characters, and contain an upper case letter,             a lower case letter and a digit'),
        ('aram485', 'Test#6^0', 'Test#6^0', b'Username is not unique. Please enter another one.'),
))
def test_register_with_invalid_input(client, username, password, cpassword, message):
    # Check that attempting to register with invalid combinations of username and password generate appropriate error
    # messages.
    response = client.post(
        '/auth/signup',
        data={'username': username, 'password': password, 'confirmPassword': cpassword}
    )
    assert message in response.data


def test_login(client, auth):
    # Check that we can retrieve the login page.
    status_code = client.get('/auth/signin').status_code
    assert status_code == 200

    # Check that a successful login generates a redirect to the homepage.
    response = auth.login()
    assert response.headers['Location'] == 'http://localhost/home'

    # Check that a session has been created for the logged-in user.
    with client:
        client.get('/home')
        assert session['username'] == 'aram485'


def test_logout(client, auth):
    # Login a user.
    auth.login()

    with client:
        # Check that logging out clears the user's session.
        auth.logout()
        assert 'user_id' not in session


def test_index(client):
    # Check that we can retrieve the home page.
    response = client.get('/home')
    assert response.status_code == 200
    assert b'Register' in response.data
    assert b'Explore' in response.data
    assert b'Login' in response.data


def test_login_required_to_review(client):
    response = client.post('/reviews/write?title=Split&year=2016')
    assert b'You need to log in to leave comments' in response.data


def test_review(client, auth):
    # Login a user.
    auth.login()

    # Check that we can retrieve the comment page.
    response = client.get('/reviews/read?title=Split&year=2016')

    assert b'Wow!' in response.data
    assert b'I love this movie so much!! It really makes you think' in response.data

    response = client.post(
        '/reviews/write?title=Split&year=2016',
        data={'rating': '6.8', 'review': 'Alright'}
    )
    assert response.headers['Location'] == 'http://localhost/reviews/read?title=Split&year=2016'

    response = client.get('/reviews/read?title=Split&year=2016')
    assert b'Alright' in response.data


@pytest.mark.parametrize(('rating', 'comment', 'messages'), (
        ('sjdf', 'Bad movie', (b'Ensure your rating is a number')),
        ('', 'Bad movie', (b'Ensure your rating is a number')),
        ('5.7', '', (b'Too short!')),
        ('', '', (b'Ensure your rating is a number')),
))
def test_comment_with_invalid_input(client, auth, rating, comment, messages):
    # Login a user.
    auth.login()

    # Attempt to comment on an article.
    response = client.post(
        '/reviews/write?title=Split&year=2016',
        data={'rating': rating,'comment': comment}
    )
    # Check that supplying invalid comment text generates appropriate error messages.
    print(response.data)
    for message in messages:
        assert message in response.data


def test_movies_with_year(client):
    # Check that we can retrieve the articles page.
    response = client.get('/movies/explore?year=2016')
    assert response.status_code == 200

    # Check that without providing a date query parameter the page includes the first article.
    assert b'Split' in response.data
    assert b'Fantastic Beasts and Where to Find Them' in response.data

    response = client.get('/movies/explore?year=2016&index=8')
    assert response.status_code == 200

    assert b'The Lost City of Z' in response.data
    assert b'Suicide Squad' in response.data

def test_user_hompepage_loggedin(client):
    # Check that we can retrieve the articles page.
    response = client.get('/user/homepage')
    assert response.status_code == 200

    # Check that all articles on the requested date are included on the page.
    assert b'Please log in' in response.data

def test_user_hompepage_not_loggedin(client, auth):
    # Login a user.
    auth.login()
    response = client.get('/user/homepage')
    assert response.status_code == 200

    # Check that all articles on the requested date are included on the page.
    assert b'Watchlist' in response.data
    assert b'History' in response.data
    assert b'My reviews' in response.data
    assert b'Sing' in response.data
    assert b'Passengers' in response.data
    assert b'I love this movie so much!! It really makes you think' in response.data


def test_watchlist_loggedin(client, auth):
    auth.login()
    response = client.get('/user/homepage')
    assert b'Mindhorn' not in response.data

    response = client.get('/movies/browse?name=Mindhorn&year=2016')
    assert b'+ Watchlist' in response.data
    response = client.get('/movies/browse?name=Mindhorn&year=2016&watchlisted=True')
    print(response.data)
    assert b'- Watchlist' in response.data

    response = client.get('/user/homepage')
    assert b'Mindhorn' in response.data

def test_remove_watchlist_loggedin(client, auth):
    auth.login()
    response = client.get('/user/homepage')
    assert b'Guardians of the Galaxy'  in response.data

    response = client.get('/movies/browse?name=Guardians+of+the+Galaxy&year=2014')
    assert b'- Watchlist' in response.data
    response = client.get('/movies/browse?name=Guardians+of+the+Galaxy&year=2014&watchlisted=False')
    print(response.data)
    assert b'+ Watchlist' in response.data

    response = client.get('/user/homepage')
    assert b'Guardians of the Galaxy' not in response.data


def test_watchlist_not_loggedin(client):
    response = client.get('/movies/browse?name=Mindhorn&year=2016')
    assert b'+ Watchlist' in response.data
    response = client.get('/movies/browse?name=Mindhorn&year=2016&watchlist=True')
    assert b'+ Watchlist' in response.data

def test_watched_loggedin(client, auth):
    auth.login()
    response = client.get('/user/homepage')
    assert b'Mindhorn' not in response.data
    response = client.get('/movies/browse?name=Mindhorn&year=2016')
    assert b'Watch' in response.data
    response = client.get('/movies/browse?name=Mindhorn&year=2016&watched=True')
    assert b'Watch' in response.data
    response = client.get('/user/homepage')
    assert b'Mindhorn' in response.data

def test_watched_not_loggedin(client):
    response = client.get('/movies/browse?name=Mindhorn&year=2016')
    assert b'Watch' in response.data
    response = client.get('/movies/browse?name=Mindhorn&year=2016&watched=True')
    assert b'Watch' in response.data

def test_search_all(client):
    response = client.get('/movies/search?query=@@')
    assert b'Split' in response.data
    assert b'Sing' in response.data
    assert b'La La Land' in response.data

def test_search_with_params(client):
    response = client.get('/movies/search?query=Action%40%40')
    assert b'The Great Wall' in response.data
    assert b'Suicide Squad' in response.data
    assert b'The Lost City of Z' in response.data
    response = client.get('/movies/search?query=Action%40Chris+Pratt%40James+Gunn')
    assert b'Guardians of the Galaxy' in response.data

def test_browse(client):
    response = client.get('/movies/browse?name=Split&year=2016')
    assert b'Cast' in response.data
    assert b'Director' in response.data
    assert b'117 minutes' in response.data
    assert b'Three girls are kidnapped by a man with a diagnosed 23 distinct personalities. They must try to escape before the apparent emergence of a frightful new 24th.' in response.data
    assert b'Explore other movies' in response.data