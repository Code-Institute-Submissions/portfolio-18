from flask import Flask, render_template, url_for, request
import os
from os import path


SECRET_KEY = os.environ.get('SECRET_KEY')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME')
MONGO_URI = os.environ.get('MONGO_URI')


app = Flask(__name__)

# Home page

@app.route('/', methods=['GET', 'POST'])\
@app.route('/index', methods=['GET', 'POST'])
def home_page():
    return render_template('layout/index.html')

@app.route("/about")
def about():
    return render_template("pages/about.html", page_title="About me")

@app.route("/skills")
def skills():
    return render_template('pages/skills.html' , page_title="Skills") 

@app.route("/contact")
def contact():
    return render_template('pages/contact.html', page_title="Contact me")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
         return render_template('pages/login.html')
  

@app.route("/register")
def register():
    return render_template('pages/register.html')



if __name__ == '__main__':
    app.run(host=os.environ.get('HOSTNAME'),
            port=os.environ.get('PORT'),
            debug=os.environ.get('DEV'))