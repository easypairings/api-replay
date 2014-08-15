from __future__ import absolute_import, print_function, unicode_literals
from datetime import datetime, timedelta

from flask.ext.rq import job
from rq_scheduler import Scheduler

from .core import redis_store, setup_app
from .exceptions import BadResponseException
from .models import Destination, Request

import requests


@job
def replay_request(request_id, destination_id, retries=None):
    '''Replays request from source to destination, retrying when appropriate'''
    app = setup_app()
    if retries is None:
        retries = app.config.get('API_REPLAY_RETRIES')
    request = Request.get(request_id)
    destination = Destination.get(destination_id)
    headers = {
        'X-Original-{}'.format(k): v for k, v in request.headers.items()
    }
    headers['Content-Type'] = request.headers.get('Content-Type', '')
    # TODO: add exception handling here
    response = requests.request(
        method=request.method,
        url=destination.url,
        data=request.body,
        headers=headers,
    )
    if response.status_code < 200 or response.status_code > 300:
        if retries:
            with app.app_context():
                scheduler = Scheduler(connection=redis_store.connection)
                delay = app.config.get('API_REPLAY_BASE') ** (
                    app.config.get('API_REPLAY_RETRIES') - retries
                )
                scheduler.enqueue_at(
                    datetime.utcnow() + timedelta(seconds=delay),
                    replay_request,
                    request.id,
                    destination.id,
                    retries=retries - 1,
                )
        else:
            raise BadResponseException(response.status_code, response.text)
