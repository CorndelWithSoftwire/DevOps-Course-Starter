from flask import Flask
from werkzeug.utils import import_string
from config import config


def create_app(config_name=None):

    # create and configure the app
    app = Flask(__name__)
    if config_name is not None:
        app.config.from_object(config[config_name])
    else:
        app.config.from_object(config['default'])

    with app.app_context():
        # attach routes
        from .index.views import index
        app.register_blueprint(index)

        return app
