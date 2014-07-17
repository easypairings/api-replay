#!/usr/bin/env python

import sys

from distutils.core import setup
from setuptools.command.test import test as TestCommand


def read_file(filename):
    try:
        with open(filename) as f:
            return f.read()
    except IOError:
        return ''

# http://pytest.org/latest/goodpractises.html
class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='API Replay',
    version='0.1',
    description='API Replay',
    author='Easy Pairings',
    author_email='dev@easypairings.com',
    url='https://github.com/easypairings/api-replay',
    packages=['api_replay'],
    install_requires=[
        'argparse==1.2.1',
        'Flask-Redis==0.0.5',
        'Flask-RQ==0.2',
        'Flask-Script==2.0.5',
        'itsdangerous==0.24',
        'Jinja2==2.7.3',
        'MarkupSafe==0.23',
        'python-slugify==0.0.7',
        'redis==2.10.1',
        'requests==2.3.0',
        'rom==0.26.5',
        'rq==0.4.6',
        'six==1.7.3',
        'Unidecode==0.04.16',
        'Werkzeug==0.9.6',
        'wsgiref==0.1.2',
    ],
    entry_points={'console_scripts': [
        'api-replay = manage:manager.run',
    ]},
    tests_require=[
        'pytest',
    ],
    cmdclass = {'test': PyTest},
    license=read_file('LICENSE'),
)
