from flask import Flask
from flask import render_template

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


from app import app
app.run(debug=True)