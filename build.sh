#!/bin/bash

set -e

if [ -d dist ]; then
    rm -rf dist
fi
if [ -d build ]; then
    rm -rf build
fi
if [ -d lindh_jsonobjecy.egg-info ]; then
    rm -rf lindh_jsonobjecy.egg-info
fi

pipenv update --dev setuptools wheel twine
pipenv run python setup.py sdist bdist_wheel
pipenv run python -m twine upload dist/*
