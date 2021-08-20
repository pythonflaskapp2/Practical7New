import os

class Settings:
    host = os.environ['HOST']
    database = os.environ['DATABASE']
    user = os.environ['USERNAME']
    password = os.environ['PASSWORD']