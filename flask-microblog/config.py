#configuration variables for flask project set here
import os

class Config(object):
    #impt: value of secret key used as cryptographic key, useful to gen signatures or tokens
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'