import requests
from flask import Flask, render_template
import random
from datetime import datetime as dt
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", title="Clean Blog", subtitle="A Blog Theme by Start Bootstrap", img="home")

@app.route('/about')
def about():
    return render_template("about.html", title="About Me", subtitle="This is what I do.", img="about")

@app.route('/contact')
def contact():
    return render_template("contact.html", title="Contact Me", subtitle="Have questions? I have answers.", img="contact")
if __name__ == "__main__":
    app.run(debug=True)


