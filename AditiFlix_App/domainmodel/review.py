from datetime import datetime

from AditiFlix_App.domainmodel.movie import Movie


class Review:

    def __init__(self, movie, review_text, rating):
        if (type(rating) is not int and type(rating) is not float) or (rating < 1) or (rating > 10):
            self.__rating = None
        else:
            self.__rating = rating

        if not isinstance(movie, Movie):
            self.__movie = None
        else:
            self.__movie = movie

        if type(review_text) is not str or review_text == "":
            self.__review_text = None
        else:
            self.__review_text = review_text

        self.__timestamp: datetime = datetime.today()

    @property
    def rating(self):
        return self.__rating

    @property
    def movie(self):
        return self.__movie

    @property
    def review_text(self):
        return self.__review_text

    @property
    def timestamp(self):
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        if isinstance(timestamp, datetime):
            self.__timestamp = timestamp


    def __repr__(self):
        return f"<Rating {self.__rating}, Review {self.__review_text}>"

    def __eq__(self, other):
        if not isinstance(other, Review):
            return False
        return other.review_text == self.__review_text \
            and other.rating == self.__rating \
            and other.movie == self.__movie \
            and other.timestamp == self.__timestamp


movie = Movie("Moana", 2016)
review_text = "This movie was very enjoyable."
rating = 8
review = Review(movie, review_text, rating)

print(review.movie)
print("Review: {}".format(review.review_text))
print("Rating: {}".format(review.rating))