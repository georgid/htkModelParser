'''
Created on Jan 15, 2016

@author: joro
'''

#!/usr/bin/env python

from setuptools import setup

setup(name='htk-model-parser',
      version='0.1',
      description='modification of to package to load in python acoustic speech models created with htk. Forked from http://cmusphinx.sourceforge.net/2010/08/python-htk-converter/. Requires http://www.dabeaz.com/ply/ ',
      author='Georgi Dzhambazov',
      url='',
      packages=['htkparser','compare' ]
)