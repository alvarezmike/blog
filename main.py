from flask import Flask, render_template
import requests
import datetime


app = Flask(__name__)

# home page
@app.route('/')
def home():
    blog_url ="https://api.npoint.io/4af156202f984d3464c3"
    response = requests.get(blog_url)
    response.raise_for_status()
    all_posts = response.json()
    current_year = datetime.datetime.now().year

    return render_template("index.html", posts=all_posts, year=current_year)

#  blog-posts
@app.route('/post/<int:num>')
def post(num):
    blog_url ="https://api.npoint.io/4af156202f984d3464c3"
    response = requests.get(blog_url)
    response.raise_for_status()
    all_posts = response.json()
    current_year = datetime.datetime.now().year

    return render_template("post.html", posts=all_posts, num=num, year=current_year)


if __name__ == "__main__":
    app.run(debug=True)
