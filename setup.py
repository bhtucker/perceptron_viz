# -*- coding: utf-8 -*-
"""
    voweler
    ~~~~~~~

    Packaging
"""
from setuptools import setup, find_packages


def get_requirements(suffix=''):
    with open('requirements%s.txt' % suffix) as f:
        result = f.read().splitlines()
    return result


def get_long_description():
    with open('README.md') as f:
        result = f.read()
    return result

setup(
    name='voweler',
    version='1.3.6',
    url='https://github.com/bhtucker/perceptron_viz',
    author='Benson Tucker',
    author_email='bensontucker@gmail.com',
    description='Perceptron learning visualization app',
    long_description=get_long_description(),
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any'
)
