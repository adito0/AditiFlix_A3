from flask import Blueprint, render_template, request, redirect, url_for, session

import AditiFlix_App.helpers.helper_functions as helper

import AditiFlix_App.adapters.movie_repository as repo


home_blueprint = Blueprint(
    'home_bp', __name__)


@home_blueprint.route('/home', methods=['GET'])
def home():
    try:
        loggedin = session['username']
        print(session['username'])
        loggedin = True
    except:
        print("No user")
        loggedin = False
    movie_list = helper.get_random_movies(3, repo.repo_instance)
    return render_template(
        'home.html',
        login=url_for('authentication_bp.signin'),
        register=url_for('authentication_bp.signup'),
        explore=url_for('movie_bp.explore', year=2019, index=0),
        logout=url_for('authentication_bp.logout'),
        loggedin=loggedin
    )