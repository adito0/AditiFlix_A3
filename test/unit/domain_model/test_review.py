from AditiFlix_App.domainmodel.review import Review
from AditiFlix_App.domainmodel.movie import Movie

import pytest
from datetime import datetime
import time


@pytest.fixture
def review():
    return Review(Movie("Up", 2009), 'Review Test', 4)


def test_init(review):
    assert review.movie == Movie("Up", 2009)
    assert review.review_text == 'Review Test'
    assert review.rating == 4
    assert type(review.timestamp) == datetime
    review1 = Review(Movie("Up", 2009), 'Review Test', 11)
    review2 = Review(Movie("Up", 2009), 'Review Test', 0)
    review3 = Review(Movie("Up", 2009), '', 10)
    review4 = Review(Movie("Up", 2009), 9, 1)
    review5 = Review(Movie("", 1989), "Review Test", 8)
    assert review1.rating is None
    assert review2.rating is None
    assert review3.review_text is None
    assert review4.review_text is None
    assert repr(review5.movie) == "<Movie None, None>"
    assert repr(review1) == "<Rating None, Review Review Test>"
    assert repr(review4) == "<Rating 1, Review None>"


def test_eq(review):
    time.sleep(1)
    review1 = Review(Movie("Up", 2009), 'Review Test', 4)
    assert review1 != review
    review2 = Review(Movie("Up", 2009), 'Review Test', 0)
    review3 = Review(Movie("Up", 2009), '', 10)
    review4 = Review(Movie("Up", 2009), 9, 1)
    review5 = Review(Movie("", 1989), "Review Test", 8)
    assert review2 != review
    assert review3 != 9
    assert review4 != review
    assert review5 != review
