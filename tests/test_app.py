import pytest


@pytest.fixture
def app():
    '''Provides a configured Flask application'''
    from api_replay.core import setup_app
    return setup_app()
