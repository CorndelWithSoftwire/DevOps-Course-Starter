from flask import Flask


def create_app(test_config=None):

    # create and configure the app
    app = Flask(__name__, instance_relative_config=False)

    # configuration
    if (test_config is not None):
        app.config.from_object('config')
    else:
        app.config.from_pyfile('config.py', silent=True)

    # attach routes
    from .views.index import index
    app.register_blueprint(index)

    return app
