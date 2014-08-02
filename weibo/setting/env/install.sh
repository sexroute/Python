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

function apt_install(){
	need=$1
	i=0
	echo ${need[*]}
	until [ ${#need[@]} -le $i ]; do
		if ! dpkg -l | grep -q ${need[i]} ; then
			apt-get install ${need[i]}
		fi
		i=$(($i+1))
	done
}

function dev_set(){
	need=(mysql-server mysql-clinet python python-pip libxml2 libxslt1.1 python-dev libmysqld-dev)
	apt_install ${need}
	# apt-get install mysql-server mysql-clinet
	# apt-get install python 
	# apt-get install python-pip 
	# apt-get install libxml2 libxslt1.1 python-dev
	# apt-get install libmysqld-dev #need by MySQL-python, because of missing file: mysql_config

	
}


function virtualenv_set(){
	if grep -q 'WORKON_HOME' .profile && grep -q 'PROJECT_HOME' .profile; then
		:
	elif [ ! -f .profile ]; then
		touch .profile
	else
		echo 'export WORKON_HOME=$HOME/.virtualenvs
	export PROJECT_HOME=$HOME/Devel
	source /usr/local/bin/virtualenvwrapper.sh' >> .profile
	fi

	. ~/.profile
	if [ ! -d ~/Devel ]; then
		mkdir ~/Devel
	fi
	mkvirtualenv $1
	mkproject $1
	setvirtualenvproject /home/luxe/.virtualenvs/$1 $(pwd)
	workon $1

	# lxml dependent on libxml2,libxslt1.1,python-dev
	# Scrapy dependent on lxml,openssl
	# pip install lxml Scrapy 
	# pip install virtualenv virtualenvwrapper
	# pip install service_identity #need by pyOpenSSL 
	# pip install sinaweibopy #needed by weibo oauth2
	# pip install MySQL-python
}

function mysql_set(){
	sudo start mysql
	# mysql -uroot -proot
	# grant all privileges on mysql.* to 'root'@'%';
	# grant all privileges on *.* to 'root'@'%';
	# set password for 'root'@'%'=password('root');
	# flush privileges;
	# exit
	# sudo restart mysql
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
		virtualenv_set $2
		;;
		mysql)
		echo mysql_set
		;;
	esac
	shift
done



