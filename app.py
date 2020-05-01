from flask import Flask, render_template, redirect, url_for, request, abort, session
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
@app.route('/index', methods=['GET', 'POST'])
def home_page():    
    return render_template('pages/index.html', headTitle="Home")

# Page to add project
@app.route('/add_project')
def addproject():
    return render_template('add_project.html')

# Adding a project to the database
@app.route('/insert_project', methods=['POST'])
def insert_project():
    projects=mongo.db.projects
    if request.method == 'POST':
        form_dict = request.form.to_dict()
        projects.insert_one(form_dict)
        return redirect(url_for('see_project'))

# View all projects in the database
@app.route('/portfolio')
def see_projects():
    return render_template('portfolio.html', projects=mongo.db.projects.find())



# Portfolio - cards presentation page
@app.route("/portfolio")
def portfolio():
    portfolio=mongo.db.projects.find()
    return render_template("pages/portfolio.html", headTitle="Portfolio", portfolio="portfolio")  

# View page 
@app.route('/presentation/project_id=<id>', methods=['POST', 'GET'])
def presentation(id):
    print_post=request.form.get('presentation')
    presentation = mongo.db.projects.find_one({"_id": ObjectId(id)})
    if request.method == 'POST':
        mongo.db.projects.find_one_and_update({"_id": ObjectId(id)},{
                    '$push':{'review':{
                    'name': session['name'],
                    'post': print_post
                    }
                }
            }
        )
        return redirect(url_for('presentation', id=id))
    mongo.db.projects.find_one_and_update({"_id": ObjectId(id)}, {"$inc": {"views": 1}})
    return render_template('pages/presentation.html', headTitle="Project", presentation="presentation")

# Contact page
@app.route("/contact", methods=['GET', 'POST'])
def contact():
    return render_template("pages/contact.html", headTitle="Contact me")

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET': 
        return render_template('pages/login.html', headTitle="Login")
    else:
        user = mongo.db.user
        login_user = user.find_one({
        'email': request.form.get('email'), 
        'password':request.form.get('password'
        )})
        
        if login_user:
            session['email'] = login_user['email']
            session['name'] = login_user['name']
        return redirect(url_for('admin'))
       
    return 'Invalid username or password combination'
       
    
@app.route('/register', methods=['POST', 'GET'])
def register():
    email = session.get('email')
    if email:
      return redirect(url_for('login'))
    user = None
    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = {'name': name, 'email': email, 'password': password}
        if mongo.db.user.find_one({"email": email}):
            return render_template('pages/register.html')
        else:
            mongo.db.user.insert_one(user)
            return render_template('pages/login.html')

    return render_template('pages/register.html', headTitle="Register")

@app.route("/logout")
def logout():
    session['email'] = None
    session['name'] = None
    return redirect(url_for('home_page'))

@app.route("/admin")
def admin():
    projects=mongo.db.projects.find({'name':session.get('name')})
    email = session.get('email')

    return render_template('pages/admin.html',projects=projects, headTitle="Admin panel")


# No permission page
@app.route('/permission-denied')
def permission_denied():
    return render_template("pages/permission.html", active="errorPage", loggedIn=False)

# 404 - Page not found
@app.errorhandler(404) 
def pageNotFound(e): 
    """ Displays custom 404 page if url isn't recognised """ 
    return render_template("pages/404.html", headTitle="Page not found", active="errorPage", loggedIn=False)


if __name__ == '__main__':
    app.run(host=os.environ.get('HOSTNAME'),
            port=os.environ.get('PORT'),
            debug=os.environ.get('DEV'))