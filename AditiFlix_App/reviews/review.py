from flask import Blueprint, render_template, request, redirect, url_for, session
import AditiFlix_App.reviews.services as services
import AditiFlix_App.adapters.movie_repository as repo


from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, SubmitField, FloatField
from wtforms.validators import DataRequired, Length, ValidationError

review_blueprint = Blueprint(
    'review_bp', __name__,url_prefix='/reviews')


@review_blueprint.route('/read', methods=['GET'])
def read():
    title = request.args.get('title')
    year = int(request.args.get('year'))
    movie = services.get_movie(title, year, repo.repo_instance)
    review_list = services.get_reviews(movie, repo.repo_instance)
    print(review_list)
    return render_template(
        'read.html',
        movie=movie,
        reviews=review_list
    )

@review_blueprint.route('/write', methods=['GET','POST'])
def write():
    form = ReviewForm()
    error = False
    title = request.args.get('title')
    print(title)
    year = int(request.args.get('year'))
    try:
        loggedin = session['username']
    except:
        loggedin = False
    print("L",loggedin)
    if form.validate_on_submit():
        try:
            services.write_review(title, year,form.review.data, float(form.rating.data), loggedin, repo.repo_instance)
            return redirect(url_for('review_bp.read',title=str(title), year=str(year)))
        except:
            error = "Enter valid rating."
    return render_template(
        'write.html',
        form=form,
        error=error,
        redirect=url_for('review_bp.write',title=title, year=str(year)),
        loggedin=loggedin,
        login=url_for('authentication_bp.signin')
    )

class ReviewForm(FlaskForm):
    review = TextAreaField('Review', [
        DataRequired(message="Too short!")])
    rating = FloatField('Rating', [
        DataRequired(message="Ensure your rating is a number")])
    submit = SubmitField('Submit')