from flask import render_template
from app import app

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