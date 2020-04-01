from flask import Flask, render_template, url_for


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/")
def about():
    return render_template('about.html') 

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5000,
            debug=True)