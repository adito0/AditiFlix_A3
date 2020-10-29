from AditiFlix_App.adapters.datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from AditiFlix_App.domainmodel.genre import Genre
from AditiFlix_App.domainmodel.actor import Actor
from AditiFlix_App.domainmodel.director import Director
from AditiFlix_App.domainmodel.movie import Movie


# def test_movies():
#     movie_file_reader = MovieFileCSVReader('../../data/Data1000Movies.csv')
#     movie_file_reader.read_csv_file()
#     movie1 = Movie("Guardians of the Galaxy", 2014)
#     movie1.description = "A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe."
#     movie1.runtime_minutes = 121
#     movie1.votes = 757074
#     movie1.rating = 8.1
#     movie1.add_genre(Genre("Action"))
#     movie1.add_genre(Genre("Adventure"))
#     movie1.add_genre(Genre("Sci-Fi"))
#     movie1.add_actor(Actor("Chris Pratt"))
#     movie1.add_actor(Actor("Vin Diesel"))
#     movie1.add_actor(Actor("Bradley Cooper"))
#     movie1.add_actor(Actor("Zoe Saldana"))
#     movie1.director = Director("James Gunn")
#     assert movie_file_reader.dataset_of_movies[0] == movie1
#     assert movie_file_reader.dataset_of_movies[0].runtime_minutes == movie1.runtime_minutes
#     assert movie_file_reader.dataset_of_movies[0].description == movie1.description
#     assert movie_file_reader.dataset_of_movies[0].votes == movie1.votes
#     assert movie_file_reader.dataset_of_movies[0].rating == movie1.rating
#     assert movie_file_reader.dataset_of_movies[0].actors == movie1.actors
#     assert movie_file_reader.dataset_of_movies[0].genres == movie1.genres
#     assert movie_file_reader.dataset_of_movies[0].director == movie1.director
#     assert movie_file_reader.dataset_of_actors[0] == Actor("Chris Pratt")
#     assert movie_file_reader.dataset_of_actors[1] == Actor("Vin Diesel")
#     assert movie_file_reader.dataset_of_actors[2] == Actor("Bradley Cooper")
#     assert movie_file_reader.dataset_of_actors[3] == Actor("Zoe Saldana")
#     assert repr(movie_file_reader.dataset_of_actors[0].actor_colleague_list) == "[<Actor Vin Diesel>, <Actor Bradley Cooper>, <Actor Zoe Saldana>, <Actor Jennifer Lawrence>, <Actor Michael Sheen>, <Actor Laurence Fishburne>, <Actor Denzel Washington>, <Actor Ethan Hawke>, <Actor Vincent D'Onofrio>, <Actor Bryce Dallas Howard>, <Actor Ty Simpkins>, <Actor Judy Greer>, <Actor Will Ferrell>, <Actor Elizabeth Banks>, <Actor Will Arnett>, <Actor Jessica Chastain>, <Actor Joel Edgerton>, <Actor Mark Strong>, <Actor Channing Tatum>, <Actor Rosario Dawson>, <Actor Jenna Dewan Tatum>]"
#     assert movie_file_reader.dataset_of_directors[0] == Director("James Gunn")
#     assert movie_file_reader.dataset_of_genres[0] == Genre("Action")
#     assert movie_file_reader.dataset_of_genres[1] == Genre("Adventure")
#     assert movie_file_reader.dataset_of_genres[2] == Genre("Sci-Fi")


