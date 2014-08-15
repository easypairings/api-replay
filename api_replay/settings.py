from os import environ as env

from .utils import DOES_NOT_EXIST

API_REPLAY_RETRIES = int(env.get('API_REPLAY_RETRIES', 10))
API_REPLAY_BASE = int(env.get('API_REPLAY_BASE', 2))
DEBUG = env.get('DEBUG', True)
REDIS_URL = env.get('REDIS_URL', DOES_NOT_EXIST)
RQ_DEFAULT_URL = env.get('RQ_DEFAULT_URL', DOES_NOT_EXIST)
SECRET_KEY = env.get('SECRET_KEY', DOES_NOT_EXIST)
