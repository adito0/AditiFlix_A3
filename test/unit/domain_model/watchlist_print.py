from AditiFlix_App.domainmodel import WatchList
from AditiFlix_App.domainmodel import Movie


def constructor_test():
    watchlist = WatchList()
    print(watchlist.size())
    watchlist.add_movie(Movie("Up", 2009))
    print(watchlist.size())
    watchlist.add_movie(Movie("Down", 1999))
    print(watchlist.size())
    watchlist.add_movie(Movie("XYZ", 2013))
    print(watchlist.size())
    watchlist.add_movie(Movie("Anabelle", 2020))
    print(watchlist.size())
    watchlist.add_movie(Movie("Anabelle", 2020))
    print(watchlist.size())

    i = iter(watchlist)
    print(next(i))
    print(next(i))
    print(next(i))

    for movie in i:
        print(movie)

    watchlist.remove_movie(Movie("Up", 2009))
    print(watchlist.size())
    watchlist.remove_movie(Movie("Left", 2009))
    print(watchlist.size())
    print(watchlist.select_movie_to_watch(0))
    print(watchlist.select_movie_to_watch(4))
    print(watchlist.first_movie_in_watchlist())
    watchlist.remove_movie(Movie("Down", 1999))
    watchlist.remove_movie(Movie("XYZ", 2013))
    watchlist.remove_movie(Movie("Anabelle", 2020))
    print(watchlist.first_movie_in_watchlist())




constructor_test()