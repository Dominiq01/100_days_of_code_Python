import requests
from flask import Flask, render_template
import random
from datetime import datetime as dt
app = Flask(__name__)


@app.route('/')
def home():
    res_blog = requests.get("https://api.npoint.io/17f039dcd895b2ae9f28")
    res_blog.raise_for_status()
    posts_data = res_blog.json()
    print(posts_data)
    date = dt.now()
    formatted_date = date.strftime("%A %d, %Y")
    return render_template("index.html", title="Dominik Blog", subtitle="A Blog created by Dominik", img="../static/assets/img/home-bg.jpg", posts=posts_data, date=formatted_date)

@app.route('/post/<post_id>')
def get_post(post_id):
    res_blog = requests.get("https://api.npoint.io/17f039dcd895b2ae9f28")
    res_blog.raise_for_status()
    posts_data = res_blog.json()
    post = [post_data for post_data in posts_data if post_data["id"] == int(post_id)][0]
    return render_template("post.html", title=post["title"], subtitle=post["subtitle"], img=post["image_url"], blog_post=post)

@app.route('/about')
def about():
    return render_template("about.html", title="About Me", subtitle="This is what I do.", img="../static/assets/img/about-bg.jpg")

@app.route('/contact')
def contact():
    return render_template("contact.html", title="Contact Me", subtitle="Have questions? I have answers.", img="../static/assets/img/contact-bg.jpg")
if __name__ == "__main__":
    app.run(debug=True)


