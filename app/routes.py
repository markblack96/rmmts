from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Test User'}
    return render_template('index.html', title='Home', user=user)

@app.route('/register')
def register():
    pass

@app.route('/login')
def login():
    render_template('login.html') 
