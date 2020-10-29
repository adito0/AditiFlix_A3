# from AditiFlix_App.domainmodel.user import User
#
#
# class Stats:
#
#     def __init__(self, user: User):
#         self.__user = user
#         self.__watched_directors = dict()
#         self.__watched_actors = dict()
#         self.__watched_genres = dict()
#         self.__watched_movies = []
#         self.update_watched_lists()
#         self.__recs = dict()
#
#     @property
#     def user(self):
#         return self.__user
#
#     @property
#     def watched_movies(self):
#         return self.__watched_movies
#     @property
#     def watched_directors(self):
#         return self.__watched_directors
#
#     @property
#     def watched_actors(self):
#         return self.__watched_actors
#
#     @property
#     def watched_genres(self):
#         return self.__watched_genres
#
#     def update_watched_lists(self):
#         for movie in self.__user.watched_movies:
#             if not(movie in self.__watched_movies):
#                 self.__watched_movies.append(movie)
#                 director = movie.director
#                 if director in self.__watched_directors:
#                     self.__watched_directors[director] += 1
#                 else:
#                     self.__watched_directors[director] = 1
#
#                 actors = movie.actors
#                 for actor in actors:
#                     if actor in self.__watched_actors:
#                         self.__watched_actors[actor] += 1
#                     else:
#                         self.__watched_actors[actor] = 1
#
#                 genres = movie.genres
#                 for genre in genres:
#                     if genre in self.__watched_genres:
#                         self.__watched_genres[genre] += 1
#                     else:
#                         self.__watched_genres[genre] = 1
#
#     def top_actors(self, number):
#         ranked_list = []
#         ranked = {k: v for k, v in sorted(self.__watched_actors.items(), key=lambda item: item[1])}
#         for i in ranked:
#             ranked_list.append(i)
#         ranked_list.reverse()
#         if type(number) == int and number > 0:
#             if number <= len(ranked_list):
#                 return ranked_list[:number]
#             else:
#                 return []
#         else:
#             return ranked_list
#
#     def top_directors(self, number):
#         ranked_list = []
#         ranked = {k: v for k, v in sorted(self.__watched_directors.items(), key=lambda item: item[1])}
#         for i in ranked:
#             ranked_list.append(i)
#         ranked_list.reverse()
#         if type(number) == int and number > 0:
#             if number <= len(ranked_list):
#                 return ranked_list[:number]
#             else:
#                 return []
#         else:
#             return ranked_list
#
#     def top_genres(self, number):
#         ranked_list = []
#         ranked = {k: v for k, v in sorted(self.__watched_genres.items(), key=lambda item: item[1])}
#         for i in ranked:
#             ranked_list.append(i)
#         ranked_list.reverse()
#         if type(number) == int and number > 0:
#             if number <= len(ranked_list):
#                 return ranked_list[:number]
#             else:
#                 return []
#         else:
#             return ranked_list
#
#     def make_recommendations(self, movie_list, number):
#         actors = self.top_actors(number)
#         directors = self.top_directors(number)
#         genres = self.top_genres(number)
#         print("Genres:", genres, actors, directors)
#         for movie in movie_list:
#             if not (movie in self.__watched_movies):
#                 if movie.director in directors:
#                     print("d", movie)
#                     self.__recs[movie] = movie.rating
#                 else:
#                     for actor in movie.actors:
#                         if actor in actors:
#                             print("a", movie)
#                             self.__recs[movie] = movie.rating
#                     for genre in movie.genres:
#                         print(genre)
#                         print(genres)
#                         if genre in genres:
#                             print("g", movie)
#                             self.__recs[movie] = movie.rating
#         ranked_list = []
#         ranked = {k: v for k, v in sorted(self.__recs.items(), key=lambda item: item[1])}
#         print(ranked)
#         for i in ranked:
#             ranked_list.append(i)
#         ranked_list.reverse()
#         return ranked_list
#
#     def __repr__(self):
#         return "Stats for User {}:\n\nList of watched movies\n{}\n{}\nList of watched genres\n{}\n{}\nList of watched "\
#                "actors\n{}\n{}\nList of watched directors\n{}\n{}\n".format(self.__user.username,"*"*30,
#                                                                             self.__watched_movies, "*"*30,
#                                                                             self.__watched_genres, "*"*30,
#                                                                             self.__watched_actors, "*"*30,
#                                                                             self.__watched_directors)
#     def __eq__(self, other):
#         return self.__user == other.user and self.__watched_movies == other.watched_movies
#     # def populate_actors_directors_genres(self, list_of_movies):
#     #     for movie in list_of_movies:
#     #         if movie.director not in self.__watched_directors and movie.director is not None:
#     #             self.__watched_directors.append(movie.director)
#     #         for actor in movie.actors:
#     #             if actor not in self.__watched_actors and actor is not None:
#     #                 self.__watched_actors.append(actor)
#     #         for genre in movie.genres:
#     #             if genre not in self.__watched_genres and genre is not None:
#     #                 self.__watched_genres.append(genre)
#


from AditiFlix_App.domainmodel.user import User


class Stats:

    def __init__(self, user: User):
        self.__user = user
        self.__watched_directors = dict()
        self.__watched_actors = dict()
        self.__watched_genres = dict()
        self.__watched_movies = []
        self.update_watched_lists()
        self.__recs = dict()

    @property
    def user(self):
        return self.__user

    @property
    def watched_movies(self):
        return self.__watched_movies
    @property
    def watched_directors(self):
        return self.__watched_directors

    @property
    def watched_actors(self):
        return self.__watched_actors

    @property
    def watched_genres(self):
        return self.__watched_genres

    def update_watched_lists(self):
        for movie in self.__user.watched_movies:
            if not(movie in self.__watched_movies and movie is not None):
                self.__watched_movies.append(movie)
                if movie.director is not None:
                    director = movie.director
                    if director in self.__watched_directors:
                        self.__watched_directors[director] += 1
                    else:
                        self.__watched_directors[director] = 1

                actors = movie.actors
                for actor in actors:
                    if actor is not None:
                        if actor in self.__watched_actors:
                            self.__watched_actors[actor] += 1
                        else:
                            self.__watched_actors[actor] = 1

                genres = movie.genres
                for genre in genres:
                    if genre is not None:
                        if genre in self.__watched_genres:
                            self.__watched_genres[genre] += 1
                        else:
                            self.__watched_genres[genre] = 1

    def top_actors(self, number):
        ranked_list = []
        ranked = {k: v for k, v in sorted(self.__watched_actors.items(), key=lambda item: item[1])}
        for i in ranked:
            ranked_list.append(i)
        ranked_list.reverse()
        if type(number) == int and number > 0:
            if number <= len(ranked_list):
                return ranked_list[:number]
            else:
                return []
        else:
            return ranked_list

    def top_directors(self, number):
        ranked_list = []
        ranked = {k: v for k, v in sorted(self.__watched_directors.items(), key=lambda item: item[1])}
        for i in ranked:
            ranked_list.append(i)
        ranked_list.reverse()
        if type(number) == int and number > 0:
            if number <= len(ranked_list):
                return ranked_list[:number]
            else:
                return []
        else:
            return ranked_list

    def top_genres(self, number):
        ranked_list = []
        ranked = {k: v for k, v in sorted(self.__watched_genres.items(), key=lambda item: item[1])}
        for i in ranked:
            ranked_list.append(i)
        ranked_list.reverse()
        if type(number) == int and number > 0:
            if number <= len(ranked_list):
                return ranked_list[:number]
            else:
                return []
        else:
            return ranked_list

    def make_recommendations(self, movie_list, number):
        actors = self.top_actors(number)
        directors = self.top_directors(number)
        genres = self.top_genres(number)
        print("G", genres)
        for movie in movie_list:
            if not (movie in self.__watched_movies):
                if movie.director in directors:
                    self.__recs[movie] = movie.rating
                else:
                    for actor in movie.actors:
                        if actor in actors:
                            self.__recs[movie] = movie.rating
                    for genre in movie.genres:
                        print(genre)
                        print(genres)
                        if genre in genres:
                            self.__recs[movie] = movie.rating
        ranked_list = []
        ranked = {k: v for k, v in sorted(self.__recs.items(), key=lambda item: item[1])}
        for i in ranked:
            ranked_list.append(i)
        ranked_list.reverse()
        return ranked_list

    # def populate_actors_directors_genres(self, list_of_movies):
    #     for movie in list_of_movies:
    #         if movie.director not in self.__watched_directors and movie.director is not None:
    #             self.__watched_directors.append(movie.director)
    #         for actor in movie.actors:
    #             if actor not in self.__watched_actors and actor is not None:
    #                 self.__watched_actors.append(actor)
    #         for genre in movie.genres:
    #             if genre not in self.__watched_genres and genre is not None:
    #                 self.__watched_genres.append(genre)

