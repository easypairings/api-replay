from flask import Flask
from flask.ext.redis import Redis

from .utils import check_required_settings


app = Flask(__name__)
redis_store = Redis()


def setup_app():
    app.config.from_object('api_replay.settings')
    check_required_settings(app.config)
    redis_store.init_app(app)
    from . import views  # NOQA registers the routes
    return app
