#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

name_ = 'lindh-jsonobject'
version_ = '1.3.3'
packages_ = [
    'lindh.jsonobject',
]

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: POSIX",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python :: 3",
]

setup(
    name=name_,
    version=version_,
    author='Johan Egneblad',
    author_email='johan@DELETEMEegneblad.se',
    description='JSON serializable objects',
    license="MIT",
    url='https://github.com/eblade/'+name_,
    download_url=('https://github.com/eblade/%s/archive/v%s.tar.gz'
                  % (name_, version_)),
    packages=packages_,
    install_requires=[],
    classifiers=classifiers,
)
