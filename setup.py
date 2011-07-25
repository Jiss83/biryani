#! /usr/bin/env python
# -*- coding: utf-8 -*-


# Biryani -- A conversion and validation toolbox
# By: Emmanuel Raviart <eraviart@easter-eggs.com>
#
# Copyright (C) 2009, 2010, 2011 Easter-eggs
# http://packages.python.org/biryani/
#
# This file is part of Biryani.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Toolbox to convert and validate values (for web forms, etc)"""


try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


classifiers = """\
Development Status :: 3 - Alpha
Environment :: Web Environment
Intended Audience :: Information Technology
License :: OSI Approved :: Apache Software License
Operating System :: OS Independent
Programming Language :: Python
"""

doc_lines = __doc__.split('\n')


setup(
    name = 'Biryani',
    version = '0.5',

    author = 'Emmanuel Raviart',
    author_email = 'eraviart@easter-eggs.com',
    classifiers = [classifier for classifier in classifiers.split('\n') if classifier],
    description = doc_lines[0],
    keywords = 'conversion form python validation web',
    license = 'http://www.apache.org/licenses/LICENSE-2.0',
    long_description = '\n'.join(doc_lines[2:]),
    url = 'http://packages.python.org/biryani/',

    install_requires = [],
    packages = find_packages(exclude = ['ez_setup']),
    zip_safe = False,
    )
