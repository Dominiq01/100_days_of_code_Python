import random
from flask import Flask, render_template, request, redirect, url_for
from add_book import AddBook
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float



class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.secret_key = "some secret string"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)

@app.route('/')
def home():
    with app.app_context():
        results = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = results.scalars().all()
        books_count = len(all_books)
        print(all_books)
    return render_template("index.html", all_books=all_books, books_count=books_count)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddBook()
    if request.method == "POST":
        name = request.form['name']
        author = request.form['author']
        rating = request.form['rating']

        with app.app_context():
            new_book = Book(title=name, author=author, rating=float(rating))
            print(new_book)
            db.session.add(new_book)
            db.session.commit()
        return redirect("/")
    return render_template("add.html", form=form)

@app.route("/delete/<book_id>")
def delete(book_id):
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        db.session.delete(book_to_delete)
        db.session.commit()
        return redirect("/")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

