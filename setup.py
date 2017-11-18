#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup, Command
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Package meta-data.
NAME = 'FacebookTools'
DESCRIPTION = 'Python module for doing batch tasks on your Facebook profile.'
URL = 'https://github.com/justani98/FacebookTools'
EMAIL = 'justani98@gmail.com'
AUTHOR = 'Aniruddh Dubey'
REQUIRED = [
    'selenium',
]

setup(
    name=NAME,
    version='0.0.1',
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
