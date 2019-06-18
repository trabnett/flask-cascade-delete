import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI ='postgresql://localhost/delete_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False