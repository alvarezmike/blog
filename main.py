from flask import Flask, render_template
import requests
import datetime


app = Flask(__name__)

# home page
@app.route('/')
def home():
    blog_url ="https://gist.githubusercontent.com/gellowg/389b1e4d6ff8effac71badff67e4d388/raw/fc31e41f8e1a6b713eafb9859f3f7e335939d518/data.json"
    response = requests.get(blog_url)
    response.raise_for_status()
    all_posts = response.json()
    current_year = datetime.datetime.now().year

    return render_template("index.html", posts=all_posts, year=current_year)

#  blog-posts
@app.route('/post/<int:num>')
def post(num):
    blog_url ="https://gist.githubusercontent.com/gellowg/389b1e4d6ff8effac71badff67e4d388/raw/fc31e41f8e1a6b713eafb9859f3f7e335939d518/data.json"
    response = requests.get(blog_url)
    response.raise_for_status()
    all_posts = response.json()
    current_year = datetime.datetime.now().year

    return render_template("post.html", posts=all_posts, num=num, year=current_year)

@app.route("/about")
def about():
    current_year = datetime.datetime.now().year

    return render_template("about.html", year=current_year)


@app.route("/contact")
def contact():
    current_year = datetime.datetime.now().year
    return render_template("contact.html", year=current_year)

if __name__ == "__main__":
    app.run(debug=True)
