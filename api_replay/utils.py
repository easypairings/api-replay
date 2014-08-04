# Much of this code was adapted from
# https://github.com/PyGotham/pygotham/blob/master/pygotham/utils.py

from os import environ as env

from .exceptions import MissingSettingsException


DOES_NOT_EXIST = env.get('DOES_NOT_EXIST', '!@DNE@!')

REQUIRED_SETTINGS = (
    'REDIS_URL',
    'RQ_DEFAULT_URL',
    'SECRET_KEY',
)


def check_required_settings(config):
    missing_settings = filter(
        lambda key: config.get(key, DOES_NOT_EXIST) == DOES_NOT_EXIST,
        REQUIRED_SETTINGS,
    )
    if missing_settings:
        raise MissingSettingsException(missing_settings)
