from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Danilo'}
    posts = [
        {
            'author': {'username': 'Rosi'},
            'body': 'Semana de p2 na ufabc'
        },
        {
            'author': {'username': 'Danilo'},
            'body': 'Final de ano'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)