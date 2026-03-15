from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from rate_movie_form import RateMovieForm
from add_movie_form import AddMovieForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db.init_app(app)


# CREATE TABLE

class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)
    ranking: Mapped[float] = mapped_column(nullable=False)
    review: Mapped[str] = mapped_column(nullable=False)
    img_url: Mapped[str] = mapped_column(nullable=False)


@app.route("/")
def home():
    with app.app_context():
        results = db.session.execute(db.select(Movie).order_by(Movie.ranking))
        all_movies = results.scalars().all()
        books_count = len(all_movies)
        print(all_movies)
    return render_template("index.html", all_movies=all_movies)

@app.route("/add/<movie>", methods=['GET', 'POST'])
def add(movie=None):
    form = AddMovieForm()
    if request.method == 'POST':
        name = form.name.data
        url = "https://api.themoviedb.org/3/search/movie"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MDNlNjU3ODA5NzcwZjc0YmZjZThmOTE0NjZmNjg2YyIsIm5iZiI6MTc3MzU5ODE1MS41OTMsInN1YiI6IjY5YjZmNWM3NWQ3N2I0OWY0ZTVjOWU5MSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.GDoJjABAnYFltijimj88IgXnNloRlM1YOTKbbBAbQnc"
        }

        params = {
            "query": name,
            "include_adult": False,
            "language": "en-US",
            "page": 1
        }

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()['results']
        print(data)
        return render_template("select.html", data=data)


    with app.app_context():
        new_movie = Movie(
            title=movie['original_title'],
            year=movie['release_date'],
            description=movie['overview'],
            rating=0,
            ranking=0,
            review="",
            img_url=f"https://image.tmdb.org/t/p/w500{movie['poster_path']}"
        )
        print(new_movie)
        db.session.add(new_movie)
        db.session.commit()
    return redirect('/')

    return render_template("add.html", form=form)

@app.route("/edit/<movie_id>", methods=['GET', 'POST'])
def edit(movie_id):
    form = RateMovieForm()
    if request.method == 'POST':
        with app.app_context():
            movie_to_update = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
            movie_to_update.rating = form.rating.data
            movie_to_update.review = form.review.data
            db.session.commit()
            return redirect('/')
    return render_template("edit.html", form=form)


@app.route("/delete/<movie_id>")
def delete(movie_id):
    with app.app_context():
        movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
        db.session.delete(movie_to_delete)
        db.session.commit()
        return redirect("/")



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
