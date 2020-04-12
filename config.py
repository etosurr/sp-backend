import os


class Config(object):
    SECRET_KEY = os.environ.get('SERCET_KEY') or 'enuvid'