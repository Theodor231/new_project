from app import app
from flask import render_template
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Theodor'}
    posts = [
        {
        'author': {'username': 'Eldar'},
        'body': 'Beautiful day in Portland'
    },
        {
            'author': {'username': 'Miguel'},
            'body': 'The Avengers movie was so cool'
        },
        {
            'author': {'username': 'Ippolit'},
            'body': 'She is beautiful'
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sing In', form=form)
