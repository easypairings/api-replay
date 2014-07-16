from flask.ext.script import Manager

from api_replay.core import setup_app
from api_replay.models import Source

manager = Manager(setup_app())


@manager.option('-n', '--name', dest='name', type=unicode, required=True)
@manager.option('-d', '--destination', dest='destination', type=unicode, required=True)
def add_source(name, destination):
    Source(
        name=name,
        destination=destination,
    ).save()

if __name__ == '__main__':
    manager.run()
