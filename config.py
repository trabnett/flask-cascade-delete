import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI ='postgresql://localhost/delete_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False