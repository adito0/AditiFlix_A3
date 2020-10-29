import pytest

from AditiFlix_App.auth.services import AuthenticationException
from AditiFlix_App.domainmodel.movie import Movie
from AditiFlix_App.domainmodel.review import Review
from AditiFlix_App.movies import services as movie_services
from AditiFlix_App.auth import services as auth_services
from AditiFlix_App.reviews import services as review_services
import AditiFlix_App.helpers.helper_functions as helper
from AditiFlix_App.users import services as user_services


#### AUTH SERVICES ####

def test_can_add_user(in_memory_repo):
    new_username = 'jzkl'
    new_password = 'abcd1A23'

    auth_services.add_user(new_username, new_password, in_memory_repo)

    user_as_dict = auth_services.get_user(new_username, in_memory_repo)
    assert user_as_dict['username'] == new_username

    # Check that password has been encrypted.
    assert user_as_dict['password'].startswith('pbkdf2:sha256:')


def test_cannot_add_user_with_existing_name(in_memory_repo):
    username = 'aram485'
    password = 'abcd1A23'

    with pytest.raises(auth_services.NameNotUniqueException):
        auth_services.add_user(username, password, in_memory_repo)


def test_authentication_with_valid_credentials(in_memory_repo):
    new_username = 'pmccartney'
    new_password = 'abcd1A23'

    auth_services.add_user(new_username, new_password, in_memory_repo)

    try:
        auth_services.authenticate_user(new_username, new_password, in_memory_repo)
    except AuthenticationException:
        assert False


def test_authentication_with_invalid_credentials(in_memory_repo):
    new_username = 'pmccartney'
    new_password = 'abcd1A23'

    auth_services.add_user(new_username, new_password, in_memory_repo)

    with pytest.raises(auth_services.AuthenticationException):
        auth_services.authenticate_user(new_username, '0987654321', in_memory_repo)


#### REVIEW SERVICES ####

def test_can_get_user_for_review(in_memory_repo):
    new_username = 'aram485'
    user = review_services.get_user(new_username, in_memory_repo)
    assert Movie("Split", 2016) in user.watchlist


def test_can_get_movie_for_review(in_memory_repo):
    movie_name = "Split"
    movie_year = 2016
    movie = review_services.get_movie(movie_name, movie_year, in_memory_repo)
    assert movie.rating == 7.3


def test_get_reviews_for_movie(in_memory_repo):
    movie_name = "Split"
    movie_year = 2016
    reviews = review_services.get_reviews(Movie(movie_name, movie_year), in_memory_repo)
    print(reviews[0].review_text, reviews[1].review_text)
    assert reviews[0].review_text == "I love this movie so much!! It really makes you think"
    assert reviews[1].review_text == "Wow!"
    assert len(reviews) == 2


def test_write_review(in_memory_repo):
    review = Review(Movie("Split", 2016), "Great", 9.1)
    review_services.write_review("Split", 2016, "Great", 9.1, "aram485", in_memory_repo)
    movie_name = "Split"
    movie_year = 2016
    reviews = review_services.get_reviews(Movie(movie_name, movie_year), in_memory_repo)
    assert reviews[2].review_text == "Great"
    assert len(reviews) == 3

#### MOVIE SERVICES ####

def test_get_random_movies(in_memory_repo):
    movies = movie_services.get_random_movies(3, in_memory_repo)
    assert len(movies) == 3
    for movie in movies:
        assert isinstance(movie, Movie)

def test_can_get_movie_for_movies(in_memory_repo):
    movie_name = "Split"
    movie_year = 2016
    movie = movie_services.get_movie(movie_name, movie_year, in_memory_repo)
    assert movie.rating == 7.3

def test_get_ordered_movies(in_memory_repo):
    movies = movie_services.get_ordered_movies_for_year(0, 8, 2016, in_memory_repo)
    movies1 = movie_services.get_ordered_movies_for_year(8, 16, 2016, in_memory_repo)
    assert movies[0] == Movie("Fantastic Beasts and Where to Find Them", 2016)
    assert movies[-1] == Movie("Split", 2016)
    assert len(movies) == 8
    assert movies1[0] == Movie("Suicide Squad", 2016)
    assert movies1[-1] == Movie("The Lost City of Z", 2016)
    assert len(movies1) == 3

def test_search_movies(in_memory_repo):
    movies = movie_services.search_for_movies("Action@@", in_memory_repo)
    assert len(movies) == 4
    assert movies[0] == Movie("Guardians of the Galaxy", 2014)
    assert movies[-1] == Movie("The Lost City of Z", 2016)
    movies1 = movie_services.search_for_movies("Action@@James+Gunn", in_memory_repo)
    assert len(movies1) == 1
    assert movies1[0] == Movie("Guardians of the Galaxy", 2014)

def test_get_reviews(in_memory_repo):
    revs = movie_services.get_reviews(Movie("Split", 2016), in_memory_repo)
    assert len(revs) == 2
    assert revs[0].review_text == "I love this movie so much!! It really makes you think"
    assert revs[1].review_text == "Wow!"

def test_can_get_user_for_movies(in_memory_repo):
    new_username = 'aram485'
    user = movie_services.get_user(new_username, in_memory_repo)
    assert Movie("Split", 2016) in user.watchlist


#### HOME SERVICES ####

def test_get_random_movies_home(in_memory_repo):
    movies = helper.get_random_movies(3, in_memory_repo)
    assert len(movies) == 3
    for movie in movies:
        assert isinstance(movie, Movie)

#### USER SERVICES ####
def test_get_user_for_userbp(in_memory_repo):
    new_username = 'aram485'
    user = user_services.get_user(new_username, in_memory_repo)
    assert Movie("Split", 2016) in user.watchlist

# def test_can_add_comment(in_memory_repo):
#     article_id = 3
#     comment_text = 'The loonies are stripping the supermarkets bare!'
#     username = 'fmercury'
#
#     # Call the service layer to add the comment.
#     review_services.add_comment(article_id, comment_text, username, in_memory_repo)
#
#     # Retrieve the comments for the article from the repository.
#     comments_as_dict = review_services.get_comments_for_article(article_id, in_memory_repo)
#
#     # Check that the comments include a comment with the new comment text.
#     assert next(
#         (dictionary['comment_text'] for dictionary in comments_as_dict if dictionary['comment_text'] == comment_text),
#         None) is not None


# def test_cannot_add_comment_for_non_existent_article(in_memory_repo):
#     article_id = 7
#     comment_text = "COVID-19 - what's that?"
#     username = 'fmercury'
#
#     # Call the service layer to attempt to add the comment.
#     with pytest.raises(news_services.NonExistentArticleException):
#         news_services.add_comment(article_id, comment_text, username, in_memory_repo)
#
#
# def test_cannot_add_comment_by_unknown_user(in_memory_repo):
#     article_id = 3
#     comment_text = 'The loonies are stripping the supermarkets bare!'
#     username = 'gmichael'
#
#     # Call the service layer to attempt to add the comment.
#     with pytest.raises(news_services.UnknownUserException):
#         news_services.add_comment(article_id, comment_text, username, in_memory_repo)
#
#
# def test_can_get_article(in_memory_repo):
#     article_id = 2
#
#     article_as_dict = news_services.get_article(article_id, in_memory_repo)
#
#     assert article_as_dict['id'] == article_id
#     assert article_as_dict['date'] == date.fromisoformat('2020-02-29')
#     assert article_as_dict['title'] == 'Covid 19 coronavirus: US deaths double in two days, Trump says quarantine not necessary'
#     #assert article_as_dict['first_para'] == 'US President Trump tweeted on Saturday night (US time) that he has asked the Centres for Disease Control and Prevention to issue a ""strong Travel Advisory"" but that a quarantine on the New York region"" will not be necessary.'
#     assert article_as_dict['hyperlink'] == 'https://www.nzherald.co.nz/world/news/article.cfm?c_id=2&objectid=12320699'
#     assert article_as_dict['image_hyperlink'] == 'https://www.nzherald.co.nz/resizer/159Vi4ELuH2fpLrv1SCwYLulzoM=/620x349/smart/filters:quality(70)/arc-anglerfish-syd-prod-nzme.s3.amazonaws.com/public/XQOAY2IY6ZEIZNSW2E3UMG2M4U.jpg'
#     assert len(article_as_dict['comments']) == 0
#
#     tag_names = [dictionary['name'] for dictionary in article_as_dict['tags']]
#     assert 'World' in tag_names
#     assert 'Health' in tag_names
#     assert 'Politics' in tag_names
#
#
# def test_cannot_get_article_with_non_existent_id(in_memory_repo):
#     article_id = 7
#
#     # Call the service layer to attempt to retrieve the Article.
#     with pytest.raises(news_services.NonExistentArticleException):
#         news_services.get_article(article_id, in_memory_repo)
#
#
# def test_get_first_article(in_memory_repo):
#     article_as_dict = news_services.get_first_article(in_memory_repo)
#
#     assert article_as_dict['id'] == 1
#
#
# def test_get_last_article(in_memory_repo):
#     article_as_dict = news_services.get_last_article(in_memory_repo)
#
#     assert article_as_dict['id'] == 6

#
# def test_get_articles_by_date_with_one_date(in_memory_repo):
#     target_date = date.fromisoformat('2020-02-28')
#
#     articles_as_dict, prev_date, next_date = news_services.get_articles_by_date(target_date, in_memory_repo)
#
#     assert len(articles_as_dict) == 1
#     assert articles_as_dict[0]['id'] == 1
#
#     assert prev_date is None
#     assert next_date == date.fromisoformat('2020-02-29')
#
#
# def test_get_articles_by_date_with_multiple_dates(in_memory_repo):
#     target_date = date.fromisoformat('2020-03-01')
#
#     articles_as_dict, prev_date, next_date = news_services.get_articles_by_date(target_date, in_memory_repo)
#
#     # Check that there are 3 articles dated 2020-03-01.
#     assert len(articles_as_dict) == 3
#
#     # Check that the article ids for the the articles returned are 3, 4 and 5.
#     article_ids = [article['id'] for article in articles_as_dict]
#     assert set([3, 4, 5]).issubset(article_ids)
#
#     # Check that the dates of articles surrounding the target_date are 2020-02-29 and 2020-03-05.
#     assert prev_date == date.fromisoformat('2020-02-29')
#     assert next_date == date.fromisoformat('2020-03-05')
#
#
# def test_get_articles_by_date_with_non_existent_date(in_memory_repo):
#     target_date = date.fromisoformat('2020-03-06')
#
#     articles_as_dict, prev_date, next_date = news_services.get_articles_by_date(target_date, in_memory_repo)
#
#     # Check that there are no articles dated 2020-03-06.
#     assert len(articles_as_dict) == 0
#
#
# def test_get_articles_by_id(in_memory_repo):
#     target_article_ids = [5, 6, 7, 8]
#     articles_as_dict = news_services.get_articles_by_id(target_article_ids, in_memory_repo)
#
#     # Check that 2 articles were returned from the query.
#     assert len(articles_as_dict) == 2
#
#     # Check that the article ids returned were 5 and 6.
#     article_ids = [article['id'] for article in articles_as_dict]
#     assert set([5, 6]).issubset(article_ids)
#
#
# def test_get_comments_for_article(in_memory_repo):
#     comments_as_dict = news_services.get_comments_for_article(1, in_memory_repo)
#
#     # Check that 2 comments were returned for article with id 1.
#     assert len(comments_as_dict) == 2
#
#     # Check that the comments relate to the article whose id is 1.
#     article_ids = [comment['article_id'] for comment in comments_as_dict]
#     article_ids = set(article_ids)
#     assert 1 in article_ids and len(article_ids) == 1
#
#
# def test_get_comments_for_non_existent_article(in_memory_repo):
#     with pytest.raises(NonExistentArticleException):
#         comments_as_dict = news_services.get_comments_for_article(7, in_memory_repo)
#
#
# def test_get_comments_for_article_without_comments(in_memory_repo):
#     comments_as_dict = news_services.get_comments_for_article(2, in_memory_repo)
#     assert len(comments_as_dict) == 0
#
#
