from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/') #associates / with function below
@app.route('/index') #associates /index with function below
def index():
    user = {'username' : 'John'}
    posts = [
        {
            'author' : {'username' : 'Miguel'},
            'body' : 'Beautiful day in Spain!'
        },
        {
            'author' : {'username' : 'Chris'},
            'body' : 'Beautiful day in Singapore!'
        }
    ]
    return render_template('index.html', title = 'Home', user = user, posts = posts)

@app.route('/login', methods=['GET', 'POST']) #methods argument set otherwise only get methods accepted
def login():
    form = LoginForm()
    if form.validate_on_submit(): #when user hits submit, validators run, returns True if ok, if False, form rendered again
        #function from flask to show message to user
        flash('Login requested for user {}, remember_me = {}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title= 'Sign In', form = form)