from AditiFlix_App.domainmodel.movie import Movie


class MovieList:
    def __init__(self):
        self.__list = tuple()

    @property
    def list(self):
        return self.__list

    def add_movie(self, movie):
        if isinstance(movie, Movie):
            if movie.title is not None:
                if movie not in self.__list:
                    self.__list = list(self.__list)
                    self.__list.append(movie)
                    self.__list = tuple(self.__list)

    def remove_movie(self, movie):
        self.__list = list(self.__list)
        movie_return  = None
        if not isinstance(movie, Movie):
            return
        for i in range(len(self.__list)-1, -1, -1):
            if movie == self.__list[i]:
                self.__list.pop(i)
                movie_return = movie
        self.__list = tuple(self.__list)
        return movie_return

    def size(self):
        return len(self.__list)

    def first_movie_in_list(self):
        if self.size() < 1:
            return
        return self.__list[0]

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        self.__list = list(self.__list)
        self.__index += 1
        if self.__index < self.size():
            return self.__list[self.__index]
        else:
            raise StopIteration
            self.__index = -1
        self.__list = tuple(self.__list)

    def __eq__(self, other):
        return self.__list == other.list


