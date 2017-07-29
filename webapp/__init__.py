import os
from flask import Flask

from webapp.models.main import db 
from webapp.controllers.main import main_blueprint

def create_app(object_name):
    """
    An flask application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/
    Arguments:
        object_name: the python path of the config object,
                     e.g. project.config.ProdConfig
    """

    app = Flask(__name__)
    app.config.from_object(object_name)

    db.init_app(app)
    app.register_blueprint(main_blueprint)

    return app