import requests
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    res_blog = requests.get(blog_url)
    res_blog.raise_for_status()
    posts_data = res_blog.json()
    return render_template("index.html", posts=posts_data)

@app.route('/post/<post_id>')
def get_post(post_id):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    res_blog = requests.get(blog_url)
    res_blog.raise_for_status()
    posts_data = res_blog.json()
    print(posts_data)
    post = [post_data for post_data in posts_data if post_data["id"] == int(post_id)][0]
    print(post)
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
