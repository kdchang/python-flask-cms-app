import configparser
import os

env = os.environ.get('WEBAPP_ENV', 'dev')
config = configparser.ConfigParser()
config.read('webapp/config.ini')

class Config(object):
    SECRET_KEY = config['DEFAULT']['secret_key']
    SESSION_SUPER_KEY = config['DEFAULT']['session_super_key']
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static/uploads/')    
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

    SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@{}:{}/{}'.format(config[env]['db_user'], config[env]['db_password'], config[env]['db_ip'], config[env]['db_port'], config[env]['db_name'])
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    GOOGLE_ID = config['DEFAULT']['google_id']
    GOOGLE_SECRET = config['DEFAULT']['google_secret']
    FACEBOOK_APP_ID = config['DEFAULT']['facebook_app_id']
    FACEBOOK_APP_SECRET = config['DEFAULT']['facebook_app_secret']

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
