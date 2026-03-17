from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from random import randint
from sqlalchemy import func

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(cafe):
        return {
            'can_take_calls': cafe.can_take_calls,
            'coffee_price': cafe.coffee_price,
            'has_sockets': cafe.has_sockets,
            'has_toilet': cafe.has_toilet,
            'has_wifi': cafe.has_wifi,
            'id': cafe.id,
            'img_url': cafe.img_url,
            'location': cafe.location,
            'map_url': cafe.map_url,
            'name': cafe.name,
            'seats': cafe.seats,
        }


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route('/random', methods=['GET'])
def random():
    if request.method == 'GET':
        with app.app_context():
            random_cafe = db.session.query(Cafe).order_by(func.random()).first()
            cafe_to_dict = Cafe.to_dict(random_cafe)
            return jsonify({"cafe": cafe_to_dict})

@app.route('/all', methods=['GET'])
def all():
    if request.method == 'GET':
        with app.app_context():
            results = db.session.execute(db.select(Cafe))
            all_cafes = results.scalars().all()
            print(all_cafes)
            cafe_dict = []
            for cafe in all_cafes:
                print(cafe.name)
                cafe_to_dict = Cafe.to_dict(cafe=cafe)
                cafe_dict.append(cafe_to_dict)
            return jsonify({"results": cafe_dict})

@app.route('/search', methods=['GET'])
def search():
    location = request.args.get('loc')
    if request.method == 'GET':
        with app.app_context():
            results = db.session.execute(db.select(Cafe).where(Cafe.location == location))
            print(results)
            all_cafes = results.scalars().all()
            if len(all_cafes) == 0:
                return jsonify({"error": {"Not Found": "Sorry, we don't have a cafe at that location."}})
            print(all_cafes)
            cafe_dict = []
            for cafe in all_cafes:
                print(cafe.name)
                cafe_to_dict = Cafe.to_dict(cafe=cafe)
                cafe_dict.append(cafe_to_dict)
            return jsonify({"results": cafe_dict})

# HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        with app.app_context():
            data = request.get_json()
            new_cafe = Cafe(
                name=data.get("name"),
                map_url=data.get("map_url"),
                img_url=data.get("img_url"),
                location=data.get("location"),
                seats=data.get("seats"),
                has_toilet=bool(data.get("has_toilet")),
                has_wifi=bool(data.get("has_wifi")),
                has_sockets=bool(data.get("has_sockets")),
                can_take_calls=bool(data.get("can_take_calls")),
                coffee_price=data.get("coffee_price")
            )
            db.session.add(new_cafe)
            db.session.commit()
            return jsonify(response={"success": f"Successfully added {new_cafe.name}."}), 201
# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
