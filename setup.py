"""
REST Web service for creation of view of a database
"""

# Always prefer setuptools over distutils
from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='python-web-service-flask',
    version='1.1.0',
    description='REST Web service for creation of view of a database',
    long_description=long_description,
    url=''
)
