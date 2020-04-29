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
# Home page

@app.route('/')

@app.route('/index', methods=['GET', 'POST'])
def home_page():
    
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

    if request.method == 'GET': 
        return render_template('pages/login.html', headTitle="Login")
    else:
        user = mongo.db.user
        login_user = user.find_one({
        'email': request.form.get('email'), 
        'password':request.form.get('password')})
        
        if login_user:
            session['email'] = login_user['email']
            session['name'] = login_user['name']
            return redirect(url_for('admin'))

        return 'Invalid username or password combination'
       
      

@app.route("/register", methods=['POST','GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name': request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('login'))

        return 'User already exits'

    return render_template("pages/register.html", headTitle="Register")


@app.route("/logout")
def logout():
    session['email'] = None
    session['name'] = None
    return redirect(url_for('home_page'))
   

@app.route("/admin")
def admin():
    return render_template('pages/admin.html', headTitle="Editor")

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
    return render_template("pages/404.html", headTitle="Page not found", active="errorPage", loggedIn=False)


if __name__ == '__main__':
    app.run(host=os.environ.get('HOSTNAME'),
            port=os.environ.get('PORT'),
            debug=os.environ.get('DEV'))