#configuration variables for flask project set here
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    #impt: value of secret key used as cryptographic key, useful to gen signatures or tokens
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    #fallback default for database of app.db if DATABASE_URL not set
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    #TRACK_MODIFICATIONS false as not needed (sends signal to application everytime a change is about to be made to db)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    