"""Init: Initializes app and ties all files together."""
from flask import Flask, render_template
from werkzeug.contrib.fixers import ProxyFix
from .config import BaseConfig
from .views import main

# For import *
__all__ = ['create_app']

# blueprint config
APP_BLUEPRINTS = [
    main
]


def create_app(config=None, app_name=None, blueprints=None):
    """Create the app factory."""
    if app_name is None:
        app_name = BaseConfig.PROJECT
    if blueprints is None:
        blueprints = APP_BLUEPRINTS

    print(blueprints)
    # declare flask app
    app = Flask(app_name)

    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.config['SECRET_KEY'] = BaseConfig.SECRET_KEY

    # config flask add-ons
    configure_app(app)
    configure_extensions(app)
    configure_blueprints(app, blueprints)
    configure_error_handlers(app)

    return app


def configure_app(app):
    """Configure app from object, parameter and env."""
    app.config.from_object('app.config.BaseConfig')


def configure_extensions(app):
    # db.init_app(app)
    pass


def configure_blueprints(app, blueprints):
    """Configure blueprints in views."""
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_error_handlers(app):
    """Route to error screens."""
    # 404 page
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404
