# -*- coding: utf-8 -*-
#
# This file is part of Invenio-Previewer-Demobbed
# Copyright (C) 2017 CERN
#
# Invenio-Previewer-Demobbed is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio-Previewer-Demobbed is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio-Previewer-Demobbed; if not, write to the Free
# Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
# 02111-1307, USA.

"""Invenio previewer for Demobbed visualisations."""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import os
import re

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
    'Flask',
    'six',
    'Invenio',
]

test_requirements = [
    # TODO: put package test requirements here
    'nose',
    'coverage',
]

# Get the version string.  Cannot be done with import!
with open(os.path.join('invenio_previewer_demobbed', 'version.py'), 'rt') as f:
    version = re.search(
        '__version__\s*=\s*"(?P<version>.*)"\n',
        f.read()
    ).group('version')

setup(
    name='invenio-previewer-demobbed',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    keywords='invenio-previewer-demobbed',
    license='GPLv2',
    author='Invenio collaboration',
    author_email='info@inveniosoftware.org',
    url='https://github.com/inveniosoftware/invenio-previewer-demobbed',
    packages=[
        'invenio_previewer_demobbed',
    ],
    package_dir={'invenio_previewer_demobbed':
                 'invenio_previewer_demobbed'},
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=requirements,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='nose.collector',
    tests_require=test_requirements
)
