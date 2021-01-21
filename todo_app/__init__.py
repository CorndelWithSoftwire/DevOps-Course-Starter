import os
from flask import Flask, current_app
from werkzeug.utils import import_string
from config import config


def create_app(config_name=None, overwrite_board=None):

    # create and configure the app
    app = Flask(__name__)

    if config_name is not None:
        app.config.from_object(config[config_name])
    else:
        app.config.from_object(config['default'])

    if overwrite_board is not None:
        app.config.update(TRELLO_BOARD=overwrite_board)

    with app.app_context():

        # attach routes
        from .index.views import index
        app.register_blueprint(index)

        return app
