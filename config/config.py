import os, json

class Development( object ):
    DEBUG = True
    TESTING = True

    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "unset")
    ALLOWED_EXTENSIONS = {'csv'}
    TALEGUR_URL = os.getenv("TALEGUR_URL", "unset")
    LOGIN_USERNAME = os.getenv("LOGIN_USERNAME", "unset")
    LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD", "unset")

class Production( object ):
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    CELERY_BACKEND = ''
    CELERY_BROKER_URL = ''

app_config = { 
    'development' : Development ,
    'production' : Production
}

class Test():
    UPLOAD_FOLDER = 'C:\\Users\\tong_\\Documents\\Github\\bulk.config.service\\upload_folder'
    ALLOWED_EXTENSIONS = {'csv'}
    TALEGUR_URL = "http://203.155.13.161:28140/api/"
    PAYLOAD_LOGIN = json.dumps({
        "username": "admin",
        "password": "a1t@21"
        })
    LOGIN_USERNAME = "admin"
    LOGIN_PASSWORD = "a1t@21"
