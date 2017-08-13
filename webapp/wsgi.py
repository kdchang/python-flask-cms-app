import os
from webapp import create_app

env = os.environ.get('WEBAPP_ENV', 'prod')
app = create_app('webapp.config.{}Config'.format(env.capitalize()))

if __name__ == '__main__':
    app.run()