import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'notthatsecret'
    RECAPTCHA_PUBLIC_KEY = 'TEST'
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
        username="nammflow",
        password="pythonanywheremysql",
        hostname="nammflow.mysql.pythonanywhere-services.com",
        databasename="nammflow$comments",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_RECYCLE = 299
