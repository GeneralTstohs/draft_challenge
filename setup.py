#!/usr/bin/python3
#Name:			setup.py
#Author:		Adam Stohs
#Date:			4/2018
#Purpose:		Creates Database to be used for the draft API
#Inputs:		None
#Outputs		creates the draft test database in the current directory	
#
#
#
#
#
from setuptools import setup
setup(name='draft_code',
      version='1',
      description='Code Challenge for Draft',
      url='http://github.com/',
      author='Adam Stohs',
      author_email='ajstohs@gmail.com',
      license='None',
      packages=['draft_code'],
      install_requires=[
        'requests',
        'flask',
        'flask_restful',
        'flask-jsonpify',
        'mysql',
        'SQLAlchemy'
    ],

)
