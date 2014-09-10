#!/usr/bin/env python

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='cuescience-design',
    version='0.1.0',
    description='New Admin Design for cuescience projects',
    maintainer='cuescience',
    maintainer_email='kontakt@cuescience.de',
    license="MIT",
    url='',
    packages=['cuescience_design', ],
    install_requires=[
        "Django",
    ]
)
