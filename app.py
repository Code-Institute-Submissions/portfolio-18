from flask import Flask, render_template, url_for, request
import os
from os import path


app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MONGO_URI'] = os.getenv('mongodb+srv://patrycja:<@scor81C>@firstcluster-y49uk.mongodb.net/test?retryWrites=true&w=majority')
COLLECTION_NAME = 'listingsAndReviews'


app = Flask(__name__)

# Home page

@app.route('/', methods=['GET', 'POST'])

@app.route('/index', methods=['GET', 'POST'])
def home_page():
    return render_template('pages/index.html')
    
@app.route("/about", methods=['GET', 'POST'])
def about():
    return render_template("pages/about.html", page_title="About me")

@app.route("/portfolio", methods=['GET', 'POST'])
def portfolio():
    return render_template("pages/portfolio.html", page_title="Portfolio")  

@app.route("/skills", methods=['GET', 'POST'])
def skills():
    return render_template('pages/skills.html' , page_title="Skills") 

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('pages/contact.html', page_title="Contact me")

  
@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template('pages/register.html')



if __name__ == '__main__':
    app.run(host=os.environ.get('HOSTNAME'),
            port=os.environ.get('PORT'),
            debug=os.environ.get('DEV'))