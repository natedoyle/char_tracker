from flask import Flask
from flask_pymongo import PyMongo
from flask import render_template
import create_page
app = Flask(__name__)
db = PyMongo(app)

@app.route("/")
def index():
    user = {'nickname': 'Nate'}  # fake user
    return '''
    <html>
    <head>
    <title>Home Page</title>
    </head>
    <body>
        <h1>Hello, ''' + user['nickname'] + '''</h1>
    </body>
    </html>
    '''

@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
