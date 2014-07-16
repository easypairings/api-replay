from flask import abort, request

from .core import app
from .jobs import replay_request
from .models import Request, Source

import json


# TODO: determine what methods should be allowed
@app.route('/request/<source_slug>/', methods=['GET', 'POST'])
def accept_request(source_slug):
    # TODO: replace with get_or_404
    source = Source.get_by(slug=source_slug)
    if not source:
        abort(404)
    req = Request(
        body=request.get_data(),
        headers=json.dumps(dict(request.headers)),
        method=request.method,
        source=source,
    )
    req.save()
    replay_request.delay(req.id)
    return '', 201


# TODO: add an admin view
