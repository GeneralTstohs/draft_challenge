#!/usr/bin/env bash

#insall dependencies
apt-get install -y python3-setuptools
apt-get install -y mysql-server
apt-get install -y mysql-client
apt-get install -y libmysqlclient15-dev
apt-get install -y python-mysqldb
apt-get install -y python-dev
apt-get install -y python3-dev

#Download requirements and create and populate database
python setup.py install


FLASK_APP=hello.py python3 -m flask run --host=0.0.0.0 --port=80 