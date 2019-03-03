from app import app
from flask import render_template, flash, redirect
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('/index'))
    return render_template('login.html', title='Sing In', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test psot #1'},
        {'authot': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)
