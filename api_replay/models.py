from datetime import datetime

from slugify import slugify

import rom


class Request(rom.Model):
    created = rom.DateTime(required=True, default=datetime.now)
    body = rom.Text(required=True)
    headers = rom.Json(required=True)
    status = rom.Text(required=True, default=u'Received')
    method = rom.Text(required=True)
    source = rom.ManyToOne('Source')


class Source(rom.Model):
    created = rom.DateTime(required=True, default=datetime.now)
    destination = rom.Text(required=True)
    name = rom.String(required=True)
    slug = rom.String(required=True, unique=True)
    requests = rom.OneToMany('Request')

    def __init__(self, *args, **kwargs):
        # HACK: ideally, this happens on save.
        # rom does validation on init, so we need to do it here
        kwargs.setdefault('slug', slugify(kwargs.get('name', '')))
        super(Source, self).__init__(*args, **kwargs)
