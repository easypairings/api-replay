from os import environ as env


DEBUG = env.get('DEBUG')
REDIS_URL = env.get('REDIS_URL')
RQ_DEFAULT_URL = REDIS_URL
