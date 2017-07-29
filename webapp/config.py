class Config(object):
    GOOGLE_ID = '38849957222-lagstdl79ah76t67bgj8if065ho6nujn.apps.googleusercontent.com'
    GOOGLE_SECRET = '53sCnPdIGAYWKelwHX_eSR3F'
    SECRET_KEY = 'super key'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    SQLALCHEMY_DATABASE_URI = 'mysql://root@127.0.0.1:3306/python_flask_cms_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
