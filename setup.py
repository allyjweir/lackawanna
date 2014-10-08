# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import lackawanna
version = lackawanna.__version__

setup(
    name='lackawanna',
    version=version,
    author='',
    author_email='ally.pcgf@gmail.com',
    packages=[
        'lackawanna',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.5',
    ],
    zip_safe=False,
    scripts=['lackawanna/manage.py'],
)