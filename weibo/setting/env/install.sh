#!/usr/bin/env bash


function print_usage(){
	echo "COMMAND is one of:"
	echo "  dev                  install the development tools."
	echo "  virtualenv           create python virtualenv and "
	echo "                       project in it."
	echo "  mysql                operation of mysql setting."
	echo ""
	echo "--------------------------END---------------------------"
}

if [ $# = 0 ]; then
	print_usage
	exit
fi

function dev_set(){
	sudo apt-get install mysql-server
	sudo apt-get install python 
	sudo apt-get install python-pip 
	sudo apt-get libxml2 libxslt1.1 python-dev
	# lxml dependent on libxml2,libxslt1.1,python-dev
	# Scrapy dependent on lxml,openssl
	sudo pip install lxml Scrapy 
	sudo pip install virtualenv virtualenvwrapper
	sudo pip install service_identity #need by pyOpenSSL 
	sudo pip install sinaweibopy #needed by weibo oauth2
	sudo apt-get install libmysqld-dev #need by MySQL-python, because of missing file: mysql_config
	sudo pip install MySQL-python
}


function virtualenv_set(){
	export WORKON_HOME=$HOME/.virtualenvs
	export PROJECT_HOME=$HOME/Devel
	source /usr/local/bin/virtualenvwrapper.sh

	setvirtualenvproject /home/luxe/.virtualenvs/weibo/ /home/luxe/Devel/weibo/
}

function mysql_set(){
	sudo start mysql 
}


until [ $# -eq 0 ]; do
	case $1 in
		--help|-help|-h)
		print_usage
		exit
		;;
		dev)
		dev_set
		;;
		virtualenv)
		echo virtualenv_set
		;;
		mysql)
		echo mysql_set
		;;
	esac
	shift
done



