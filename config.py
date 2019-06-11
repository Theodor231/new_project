import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 10
    MAIL_SERVER = os.environ.get('smtp@gmail.com')
    MAIL_PORT = int(os.environ.get('465') or 25)
    MAIL_USE_SSL = os.environ.get('True') is not None
    MAIL_USERNAME = os.environ.get('')
    MAIL_PASSWORD = os.environ.get('')
    ADMINS = ['']
