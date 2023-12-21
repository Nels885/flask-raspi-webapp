import os
import subprocess
import click
from flask import Flask, Blueprint

from constance import config
from constance.settings import CONFIG, CONFIG_FIELDSETS

from .utils import get_state_info, get_sys_info, get_today_date
from .api import api_bp
from .routes import main_bp


class WebApp(object):

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault('BOOTSTRAP_USE_MINIFIED', True)
        app.config.setdefault('BOOTSTRAP_CDN_FORCE_SSL', False)

        app.config.setdefault('BOOTSTRAP_QUERYSTRING_REVVING', True)
        app.config.setdefault('BOOTSTRAP_SERVE_LOCAL', False)

        app.config.setdefault('BOOTSTRAP_LOCAL_SUBDOMAIN', None)

        blueprint = Blueprint(
            'webapp',
            __name__,
            template_folder='templates',
            static_folder='static',
            static_url_path=app.static_url_path + '/webapp')

        app.register_blueprint(blueprint)

        app.register_blueprint(api_bp)
        app.register_blueprint(main_bp)

        app.context_processor(get_today_date)
        app.context_processor(get_state_info)
        app.context_processor(get_sys_info)


def create_app(database_uri=None):

    # Initialisze l'application Flask
    app = Flask(__name__)

    # Config options - Make sure you created a 'settings.py' file.
    app.config.from_object(os.environ.get('APP_SETTINGS', 'webapp.settings'))
    # To get one variable, tape app.config['MY_VARIABLE']

    WebApp(app)

    config.init_app(app)

    return app

app = create_app()
