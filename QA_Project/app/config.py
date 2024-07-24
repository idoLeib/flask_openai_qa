import os


class Config(object):
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('QA_POSTGRES_DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
