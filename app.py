from flask import Flask, render_template, redirect, session, url_for, request, abort
import os
import bcrypt
from os import path
from werkzeug.security import generate_password_hash, check_password_hash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


if path.exists('venv.py'):
    import venv

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

# Home page
@app.route('/')

# Index page
@app.route('/', methods=['GET', 'POST'])
def home_page():    
    return render_template('pages/index.html', headTitle="Home")


# Adding a project to the database
@app.route('/insert_project', methods=['POST'])
def insert_project():
    projects=mongo.db.projects
    if request.method == 'POST':
        form_dict = request.form.to_dict()
        projects.insert_one(form_dict)
        return redirect(url_for('admin'))

# View all projects in the database
@app.route('/portfolio')
def see_projects():
    return render_template('pages/portfolio.html', headTitle="Portfolio", projects=mongo.db.projects.find())

# Viewing a projects's information
@app.route('/project/<project_id>')
def project(project_id):
    the_project = mongo.db.projects.find_one({"_id": ObjectId(project_id)})
    return render_template('pages/project.html',  headTitle="Project", project=the_project)

# Page for user to edit review
@app.route('/project/edit/<project_id>')
def edit(project_id):       
    the_project = mongo.db.projects.find_one({"_id": ObjectId(project_id)})
    email = session.get('email')
    if not email:
        return redirect(url_for('permission_denied'))

    return render_template('pages/edit.html',  project=the_project, email=session['email'], headTitle="Edit")    

# Updating project in database
@app.route('/project/update/<project_id>', methods=["POST"])
def update(project_id): 
    projects=mongo.db.projects
    projects.update({'_id': ObjectId(project_id)},
    {
        'email': request.form.get("email"),
        'project_name': request.form.get('project_name'),
        'for_who': request.form.get('for_who'),
        'description': request.form.get('description'),
        'url': request.form.get('url'),
        'url_big':request.form.get('url'),
        'url_source':request.form.get('url_source'),
        'year_of_submission': request.form.get('year_of_submission')
    })
    return redirect(url_for('admin'))

# Deleting projects's entry from database
@app.route('/project/delete/<project_id>')
def delete(project_id):
     """ Function deleting""" 
    mongo.db.projects.remove({'_id': ObjectId(project_id)})
    return redirect(url_for('admin'))

# Contact page
@app.route("/contact", methods=['GET', 'POST'])
def contact():
    return render_template("pages/contact.html", headTitle="Contact me")

@app.route('/login', methods=['POST', 'GET'])
def login():
    """ function allowing to login to admin panel, but only with good credentials, otherwise it will be redirected to permission denied"""
    if request.method == 'GET': 
        return render_template('pages/login.html', headTitle="Login")
    else:
        user = mongo.db.user
        login_user = user.find_one({
        'email': request.form.get('email')})

    print(request.form.get('email'))
    
    if login_user:
          if request.form['password'] == login_user['password']:
                  session['email'] = request.form['email']
          return redirect(url_for('admin'))
      
    return render_template('pages/permission.html', headTitle="Access denied")
       
@app.route("/logout")
def logout():
    session['email'] = None
    session['name'] = None
    return render_template('pages/logout.html', headTitle="Logout")


@app.route("/admin")
def admin():
    """ This is function redirecting me to admin panel, but at the same time not allowing for authentication if user not in session. 
    """
    projects=mongo.db.projects.find({'email':session.get('email')})
    email = session.get('email')
    if not email:
        return redirect(url_for('login'))
    return render_template('pages/admin.html',projects=projects, headTitle="Admin panel")


# No permission page
@app.route('/permission')
def permission_denied():
    """ Function made to redirect when visitor wants to get to views permited only for admin """ 
    return render_template("pages/permission.html",active="errorPage", loggedIn=False, headTitle="Access denied")

# 404 - Page not found
@app.errorhandler(404) 
def pageNotFound(e): 
    """ Displays custom 404 page if url isn't recognised """ 
    return render_template("pages/404.html", headTitle="Page not found", active="errorPage", loggedIn=False)


if __name__ == '__main__':
    app.run(host=os.environ.get('HOSTNAME'),
            port=os.environ.get('PORT'),
            debug=os.environ.get('DEV'))