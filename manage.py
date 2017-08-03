import os
import datetime
import random

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from webapp import create_app
from webapp.models.main import db

# default to dev config
env = os.environ.get('WEBAPP_ENV', 'dev')
app = create_app('webapp.config.{}Config'.format(env.capitalize()))

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("runserver", Server())
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(
        app=app,
        db=db
    )

if __name__ == "__main__":
    manager.run()