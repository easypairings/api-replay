from flask.ext.script import Manager
from slugify import slugify

from api_replay.core import setup_app
from api_replay.models import Source

import rom

manager = Manager(setup_app())


@manager.option('-n', '--name', dest='name', type=unicode, required=True)
@manager.option('-d', '--destination', dest='destination', type=unicode, required=True)
def add_source(name, destination):
    try:
        Source(
            name=name,
            destination=destination,
        ).save()
    except rom.exceptions.UniqueKeyViolation:
        print('A source already exists with slug "{}". Try again.'.format(name))

if __name__ == '__main__':
    manager.run()
