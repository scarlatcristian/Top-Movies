from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


class EditMovie(FlaskForm):
    rating = StringField(label='Your Rating Out of 10',
                         validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired()])
    submit = SubmitField(label='Done')


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///mymovies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Create Table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(), nullable=False)
    img_url = db.Column(db.String(), nullable=False)


@app.route("/")
def home():
    all_movies = db.session.query(Movie).all()
    return render_template("index.html", movies=all_movies)


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_movie(id):
    movie_to_edit = Movie.query.get(id)
    edit_movie_form = EditMovie()
    if edit_movie_form.validate_on_submit():
        movie_to_edit.rating = float(edit_movie_form.rating.data)
        movie_to_edit.review = edit_movie_form.review.data
        db.session.commit()
        all_movies = db.session.query(Movie).all()
        return render_template('index.html', movies=all_movies)
    return render_template('edit.html', form=edit_movie_form, movie=movie_to_edit)


@app.route('/delete/<int:id>')
def delete_movie(id):
    movie_to_delete = Movie.query.get(id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

# part 4
