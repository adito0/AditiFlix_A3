from flask import Blueprint, render_template, request, redirect, url_for, session
import AditiFlix_App.movies.services as services
import AditiFlix_App.adapters.movie_repository as repo
from AditiFlix_App.domainmodel.movie import Movie

movie_blueprint = Blueprint(
    'movie_bp', __name__, url_prefix='/movies')


@movie_blueprint.route('/browse', methods=['GET'])
def browse():
    moviename = request.args.get('name')
    movie = services.get_movie(moviename, int(request.args.get('year')), repo.repo_instance)
    watched = False
    watchlisted = False
    try:
        username = session['username']
        print(request.args.get('watched'), type(request.args.get('watched')))
        user = services.get_user(username, repo.repo_instance)
        if (request.args.get('watched') == "True"):
            user.watch_movie(movie)
        if (request.args.get('watchlisted') == "True"):
            user.watchlist_movie(movie)
        elif (request.args.get('watchlisted') == "False"):
            user.remove_movie(movie)
        if movie in user.watched_movies:
            watched = True
        if movie in user.watchlist:
            watchlisted = True
        loggedin = True
    except:
        loggedin = False
        print("not logged in")
    recs = services.get_random_movies(3, repo.repo_instance)
    while movie in recs:
        recs = services.get_random_movies(3, repo.repo_instance)

    return render_template(
        'browse_movie.html',
        movie=movie,
        recs=recs,
        loggedin=loggedin,
        watched=watched,
        watchlisted=watchlisted
    )


@movie_blueprint.route('/explore', methods=['GET'])
def explore():
    print(url_for('movie_bp.explore'))
    start_index = request.args.get('index')
    year = int(request.args.get('year'))
    if start_index is None:
        start_index = 0
    start_index = int(start_index)
    print(year, start_index)
    movie_list = services.get_ordered_movies_for_year(start_index, 8, year, repo.repo_instance)
    full_length = services.get_number_movies_for_year(year, repo.repo_instance)
    if start_index == 0:
        prev = False
    else:
        prev = True
    if start_index + 8 > full_length:
        next = False
    else:
        next = True
    return render_template(
        'explore.html',
        movieList=movie_list,
        year=year,
        index=start_index,
        nextEnable=next,
        prevEnable=prev,
        this_url=url_for('movie_bp.explore')
    )


@movie_blueprint.route('/search', methods=['GET'])
def search():
    search = request.args.get('query')
    movie_list = services.search_for_movies(search, repo.repo_instance);
    if search == "@@":
        value = "ALL"
    else:
        search = search.split("@")
        for i in range(len(search) - 1, -1, -1):
            if search[i] == "":
                search.pop(i)
        search = ", ".join(search)
        search = search.replace(";", ", ")
        value = search
    return render_template(
        'search.html',
        movieList=movie_list,
        value=value
    )
