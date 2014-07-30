#!/usr/bin/env bash
sudo apt-get install python 
sudo apt-get install python-pip 
sudo apt-get libxml2 libxslt1.1 python-dev
# lxml dependent on libxml2,libxslt1.1,python-dev
# Scrapy dependent on lxml,openssl
sudo pip install lxml Scrapy 
sudo pip install python-virtualenv 
sudo pip install service_identity #need by pyOpenSSL 
sudo pip install sinaweibopy #needed by weibo oauth2

sudo apt-get install libmysqld-dev #need by MySQL-python, because of missing file: mysql_config
sudo pip install MySQL-python

