from flask import Flask, render_template, url_for
import os
from os import path
if path.exists("env.py"):
  import venv 


SECRET_KEY = os.environ.get('SECRET_KEY')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME')
MONGO_URI = os.environ.get('MONGO_URI')


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('pages/index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/skills")
def skills():
    return render_template('skills.html') 

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')






if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5000,
            debug=True)