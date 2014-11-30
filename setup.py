# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

NAME = 'pyllo'
VERSION = '0.1'

requires = ['requests']

setup(name=NAME,
      version=VERSION,
      packages=find_packages(),
      install_requires=requires)
