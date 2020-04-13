import os


class Config(object):
    SECRET_KEY = os.environ.get('SERCET_KEY') or 'enuvid'
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost:5432/sp'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

