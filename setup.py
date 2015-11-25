#!/usr/bin/env python

from distutils.core import setup
from setuptools import find_packages

setup(
  name='collectstupid',
  description='A Faster Collect Static (sometimes) for Django',
  version='15.11.6',
  long_description=open('README.md').read(),
  author='Paul Bailey',
  author_email='paul.m.bailey@gmail.com',
  packages=find_packages(),
  url='https://github.com/pizzapanther/collectstupid',
  license='MIT',
  include_package_data=True,
  install_requires=['Django>=1.7'],
  classifiers=['Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3']
)