from flask import render_template
from app import app

@app.route('/')
def home():
    return "Welcome to the Home Page. We've got fun and games"

@app.route('/about')
def about():
    return render_template('about.jinja')

@app.route('/blog')
def blog():
    return render_template('blog.jinja')

@app.route('/home')
def home():
    return render_template('home.jinja')

@app.route('/register')
def register():
    return render_template('register.jinja')