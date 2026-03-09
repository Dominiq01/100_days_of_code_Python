import requests
from flask import Flask, render_template
import random
from datetime import datetime as dt
app = Flask(__name__)


@app.route('/')
def home():
    random_num = random.randint(1,10)
    curr_year = dt.now().year
    print(curr_year)
    return render_template("index.html", year=curr_year)

@app.route('/name/<name>')
def guess_age_gender(name):
    try:
        age_res = requests.get(f"https://api.agify.io?name={name}")
        age_res.raise_for_status()
        age = age_res.json()["age"]
    except():
        print("something went wrong")

    try:
        gender_res = requests.get(f"https://api.genderize.io?name={name}")
        gender_res.raise_for_status()
        gender = gender_res.json()["gender"]
    except():
        print("something went wrong")

    return render_template("guess.html", name=name, age=age, gender=gender)

@app.route('/blog')
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    res_blog = requests.get(blog_url)
    res_blog.raise_for_status()
    posts_data = res_blog.json()
    print(posts_data)

    return render_template("blog.html", posts=posts_data)

if __name__ == "__main__":
    app.run(debug=True)


