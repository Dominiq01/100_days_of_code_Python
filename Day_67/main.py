import datetime

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
from add_post_form import AddPostForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    results = db.session.execute(db.select(BlogPost))
    all_posts = results.scalars().all()
    return render_template("index.html", all_posts=all_posts)


@app.route('/post/<post_id>', methods=['GET'])
def show_post(post_id):
    if request.method == 'GET':
        with app.app_context():
            requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    return render_template("post.html", post=requested_post)


@app.route('/add-new-post', methods=['GET', 'POST'])
def add_new_post():
    form = AddPostForm()
    today = datetime.datetime.now().strftime('%M %d, %Y')
    if request.method == 'POST' and form.validate_on_submit():
        with app.app_context():
            new_post = BlogPost(
                title=form.title.data,
                subtitle=form.subtitle.data,
                date=today,
                body=form.content.data,
                author=form.author.data,
                img_url=form.img_url.data
            )
            db.session.add(new_post)
            db.session.commit()
            return redirect('/')
    return render_template("make-post.html", form=form, title="New Post")


@app.route('/edit-post/<post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    with app.app_context():
        post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
        form = AddPostForm(title=post.title,
                           subtitle=post.subtitle,
                           img_url=post.img_url,
                           author=post.author,
                           content=post.body)
    if request.method == 'GET':
        return render_template("make-post.html", form=form, title="Edit Post")
    elif request.method == 'POST' and form.validate_on_submit():
        with app.app_context():
            post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
            post.title = form.title.data
            post.subtitle = form.subtitle.data
            post.img_url = form.img_url.data
            post.author = form.author.data
            post.body = form.content.data
            db.session.commit()
        return redirect(f'/post/{post_id}')

@app.route("/delete/<post_id>")
def delete(post_id):
    with app.app_context():
        post_to_delete = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
        db.session.delete(post_to_delete)
        db.session.commit()
        return redirect("/")

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
