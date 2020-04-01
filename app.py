
from flask import Flask, render_template, url_for
import os
from os import path
if path.exists("venv.py"):
 import venv 

SECRET_KEY = os.environ.get('SECRET_KEY')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME')
MONGO_URI = os.environ.get('MONGO_URI')


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('pages/index.html')

if __name__ == '__main__':
      app.run(host='0.0.0.0',port=5000, debug=True)
