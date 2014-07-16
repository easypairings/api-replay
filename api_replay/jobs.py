from flask.ext.rq import job

from .exceptions import BadResponseException
from .models import Request

import requests


@job
def replay_request(request_id):
    request = Request.get(request_id)
    headers = {
        'X-Original-{}'.format(k): v for k, v in request.headers.items()
    }
    headers['Content-Type'] = request.headers.get('Content-Type', '')
    response = requests.request(
        method=request.method,
        url=request.source.destination,
        data=request.body,
        headers=headers,
    )
    if response.status_code < 200 or response.status_code > 300:
        raise BadResponseException(response.status_code, response.text)
