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
