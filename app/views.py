from app import app
from flask import render_template
from .forms import DND5e

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Nate'}  # fake user
    return render_template('index.html',
                           title='Home',
                           user=user)

@app.route('/5e')
def fifth_ed():
    form = DND5e()
    return render_template('5e.html', title="Your mom", form=form)
