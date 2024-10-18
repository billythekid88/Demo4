from flask import render_template
from . import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
# add a route for hobbies.html
@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')
# add a route for career.html
@app.route('/career')
def career():
    return render_template('career.html')
# add a route for statistics.html
@app.route('/statistics')
def statistics():
    return render_template('statistics.html')