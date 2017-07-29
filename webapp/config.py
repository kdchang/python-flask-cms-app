class Config(object):
    SECRET_KEY = 'super key'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    SQLALCHEMY_DATABASE_URI = 'mysql://root@127.0.0.1:3306/python_flask_cms_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
