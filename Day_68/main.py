import os.path

from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_login import LoginManager
from sqlalchemy.exc import IntegrityError
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
login_manager = LoginManager()
login_manager.init_app(app)
# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB


class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        hashed_pass = generate_password_hash(password, method='pbkdf2', salt_length=8)
        with app.app_context():
            try:
                new_user = User(email=email, name=name, password=hashed_pass)
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user)
                return redirect('/secrets')
            except IntegrityError:
                error = "This email already exists"
    return render_template("register.html", error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        with app.app_context():
            user = db.session.execute(db.select(User).where(User.email == email)).scalar()
            if user:
                is_pass_valid = check_password_hash(user.password, password)
                print(is_pass_valid)
                if is_pass_valid:
                    login_user(user)
                    flash("You were successfully logged in!")
                    return redirect('/secrets')
                else:
                    error = "Invalid password"
            else:
                error = "There is no such email in database"

    return render_template("login.html", error=error)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/download')
@login_required
def download():
    directory = os.path.join(app.root_path, 'static', 'files')
    return send_from_directory(directory, 'cheat_sheet.pdf', as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
