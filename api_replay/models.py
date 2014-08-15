from __future__ import absolute_import, print_function, unicode_literals
from datetime import datetime

from slugify import slugify

import rom


class Request(rom.Model):
    '''Represents an HTTP request'''
    created = rom.DateTime(required=True, default=datetime.now)
    body = rom.Text(required=True)
    headers = rom.Json(required=True)
    status = rom.Text(required=True, default='Received')
    method = rom.Text(required=True)
    source = rom.ManyToOne('Source', required=True)


class Source(rom.Model):
    '''A service from which to receive requests'''
    created = rom.DateTime(required=True, default=datetime.now)
    name = rom.String(required=True)
    slug = rom.String(required=True, unique=True)
    destinations = rom.OneToMany('Destination')
    requests = rom.OneToMany('Request')

    def __init__(self, *args, **kwargs):
        # HACK: ideally, this happens on save.
        # rom does validation on init, so we need to do it here
        kwargs.setdefault('slug', slugify(kwargs.get('name', '')))
        super(Source, self).__init__(*args, **kwargs)


class Destination(rom.Model):
    '''A place to forward requests that come from a source'''
    created = rom.DateTime(required=True, default=datetime.now)
    name = rom.String(required=True)
    url = rom.String(required=True)
    source = rom.ManyToOne('Source', required=True)
