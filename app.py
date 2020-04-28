from flask import Flask, render_template, redirect, url_for, request, abort, session
import os
import bcrypt
from os import path
from werkzeug.security import generate_password_hash, check_password_hash
from flask_pymongo import PyMongo


if path.exists('venv.py'):
    import venv

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

users = mongo.db.users
# Home page

@app.route('/')

@app.route('/index', methods=['GET', 'POST'])
def home_page():
    if 'username' in session:
        return 'You are logged in as' + session['username']
    return render_template('pages/index.html', headTitle="Home")
    
@app.route("/about", methods=['GET', 'POST'])
def about():
    project= mongo.db.projects
    return render_template("pages/about.html", headTitle="About me")

@app.route("/portfolio", methods=['GET', 'POST'])
def portfolio():
    projects=mongo.db.projects.find()
    return render_template("pages/portfolio.html", headTitle="Portfolio", projects=projects)  

@app.route('/presentation')
def presentation():
    return render_template('pages/presentation.html', headTitle="Project", projects=mongo.db.projects.find())

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    return render_template("pages/contact.html", headTitle="Contact me")

@app.route("/login", methods=['GET', 'POST'])
def login():

    """ 
    Flask-Bcrypt is a Flask extension that provides bcrypt hashing utilities for your application.

    Due to the recent increased prevelance of powerful hardware, such as modern GPUs, hashes have become increasingly easy to crack. A proactive solution to this is to use a hash that was designed to be “de-optimized”. Bcrypt is such a hashing facility; unlike hashing algorithms such as MD5 and SHA1, which are optimized for speed, bcrypt is intentionally structured to be slow.

    For sensitive data that must be protected, such as passwords, bcrypt is an advisable choice.

    """
    users = mongo.db.users
    login_user = users.find_one({'name': request.form['username']})

    if login_user:
        if bcryp
    login_password = users.find_one({'password': request.form['userpassword']})

    return render_template('login.html', headTitle="Admin panel", users=users)

@app.route("/register", methods=['GET','POST'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name': request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'User already exits'

    return render_template('register.html')


@app.route("/editor")
def editor():
    return render_template('pages/editor.html', headTitle="Editor")


@app.route("/add_project")
def add_project():
    return render_template('pages/add_project.html',
    projects=mongo.db.projects.find())

@app.route("/insert_project", methods=['POST'])
def insert_project():
    projects = mongo.db.projects
    projects.insert_one(request.form.to_dict())
    return redirect(url_for('project_presentation'))




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