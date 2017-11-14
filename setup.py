#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = 'leave_fb_groups'
DESCRIPTION = 'Leave fb groups using keywords. '
URL = 'https://github.com/me/myproject'
EMAIL = 'justani98@gmail.com'
AUTHOR = 'Aniruddh Dubey'

# What packages are required for this module to be executed?
REQUIRED = [
    'selenium',
]

setup(
    name=NAME,
    version=0.0.1,
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    py_modules=['groups'],

    entry_points={
        'console_scripts': ['mycli=mymodule:cli'],
    },
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
