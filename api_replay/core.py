from flask import Flask
from flask.ext.redis import Redis
from os import environ as env
import sys

app = Flask(__name__)
redis_store = Redis()


def setup_app():
    app.config.from_object('api_replay.settings')
    if env.get('REDIS_URL') is None:
    	print "Please set REDIS_URL env var, for local testing it should be redis://localhost:6379"
    	sys.exit(1) 
    redis_store.init_app(app)
    from . import views  # NOQA registers the routes
    return app
