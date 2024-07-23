import os


class Config(object):
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
