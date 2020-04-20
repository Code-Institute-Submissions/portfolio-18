from flask import Flask, render_template, url_for, request, abort
import os
from os import path

if path.exists('env.py'):
    import venv

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MONGO_URI'] = os.getenv('MONGO_URI')
COLLECTION_NAME = 'listingsAndReviews'


# Home page

@app.route('/', methods=['GET', 'POST'])

@app.route('/index', methods=['GET', 'POST'])
def home_page():
    return render_template('pages/index.html')
    
@app.route("/about", methods=['GET', 'POST'])
def about():
    return render_template("pages/about.html", headTitle="About me")

@app.route("/portfolio", methods=['GET', 'POST'])
def portfolio():
    return render_template("pages/portfolio.html", headTitle="Portfolio")  

@app.route("/skills", methods=['GET', 'POST'])
def skills():
    return render_template('pages/skills.html' , headTitle="Skills") 

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('pages/contact.html', headTitle="Contact me")



if __name__ == '__main__':
    app.run(host=os.environ.get('HOSTNAME'),
            port=os.environ.get('PORT'),
            debug=os.environ.get('DEV'))