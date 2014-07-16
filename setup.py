#!/usr/bin/env python

from distutils.core import setup


def read_file(filename):
    try:
        with open(filename) as f:
            return f.read()
    except IOError:
        return ''


setup(
    name='API Replay',
    version='0.1',
    description='API Replay',
    author='Easy Pairings',
    author_email='dev@easypairings.com',
    url='https://github.com/easypairings/api-replay',
    packages=['api_replay'],
    install_requires=[
        'Flask-RQ==0.2',
        'Flask-Redis==0.0.5',
        'Flask-Script==2.0.5',
        'Jinja2==2.7.3',
        'MarkupSafe==0.23',
        'Unidecode==0.04.16',
        'Werkzeug==0.9.6',
        'argparse==1.2.1',
        'itsdangerous==0.24',
        'python-slugify==0.0.7',
        'redis==2.10.1',
        'requests==2.3.0',
        'rom==0.26.5',
        'rq==0.4.6',
        'six==1.7.3',
        'wsgiref==0.1.2',
    ],
    entry_points={'console_scripts': [
        'api-replay = manage:manager.run',
    ]},
    license=read_file('LICENSE'),
)
