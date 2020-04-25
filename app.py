from flask import Flask, render_template, redirect, url_for, request, abort
import os
from os import path
from flask_pymongo import PyMongo


if path.exists('venv.py'):
    import venv

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

# Home page

@app.route('/')

@app.route('/index', methods=['GET', 'POST'])
def home_page():
    return render_template('pages/index.html', headTitle="home")
    
@app.route("/about", methods=['GET', 'POST'])
def about():
    return render_template("pages/about.html", headTitle="About me")

@app.route("/portfolio", methods=['GET', 'POST'])
def portfolio():
    return render_template("pages/portfolio.html", headTitle="Portfolio")  

@app.route("/skills", methods=['GET', 'POST'])
def skills():
    return render_template('pages/skills.html' , headTitle="Skills") 

@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("pages/login.html", headTitle="Admin panel")

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    return render_template("pages/contact.html", headTitle="Contact me")

@app.route('/get_tasks')
def get_tasks():
    return render_template('pages/tasks.html', tasks=mongo.db.tasks.find())

@app.route("/add_project")
def add_project():
    return render_template('pages/tasks.html', tasks=mongo.db.tasks.find())

@app.route("/insert_project")
def insert_project():
    return render_template('pages/tasks.html', tasks=mongo.db.tasks.find())    


# No permission page
@app.route('/permission-denied')
def permission_denied():
    return render_template("pages/permission.html", active="errorPage", loggedIn=False)

@app.errorhandler(404) 
def pageNotFound(e): 
    """ Displays custom 404 page if url isn't recognised """ 
    return render_template("pages/404.html", active="errorPage", loggedIn=False)


if __name__ == '__main__':
    app.run(host=os.environ.get('HOSTNAME'),
            port=os.environ.get('PORT'),
            debug=os.environ.get('DEV'))