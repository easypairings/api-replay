from __future__ import absolute_import, print_function, unicode_literals

from flask.ext.script import Manager

from api_replay.core import setup_app
from api_replay.models import Destination, Source

import rom

manager = Manager(setup_app())


@manager.command
def add_source(name):
    '''Adds a `Source` with the specified name'''
    try:
        source = Source(name=name)
        source.save()
    except rom.exceptions.UniqueKeyViolation:
        print('A source already exists with slug {}. Try again.'.format(
            source.slug,
        ))
        return
    print('Created source {} (slug: {})'.format(source.name, source.slug))


@manager.option('-n', '--name', dest='name', required=True)
@manager.option('-s', '--source', dest='source', required=True)
@manager.option('-u', '--url', dest='url', required=True)
def add_destination(name, source, url):
    '''Adds a `Destination` with the specified name, source, and url'''
    source = Source.get_by(slug=source)
    if not source:
        print('No source found for slug {}'.format(source))
        return

    # TODO: detect duplicate destinations

    destination = Destination(
        name=name,
        source=source,
        url=url,
    )
    destination.save()

    print('Created desination {} pointing to {} for source {}'.format(
        destination.name,
        destination.url,
        source.name,
    ))


if __name__ == '__main__':
    manager.run()
