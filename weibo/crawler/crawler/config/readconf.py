from abstract import ReadConfAbstract, ConfigParser, _PubVariable

class ReadConf(ReadConfAbstract):
	"""docstring for ReadConf"""
	def __init__(self):
		super(ReadConf, self).__init__()

	def fetchNamePswd(self):
		try:
			name = self.config.get('WEIBO-OAuth2','USER_NAME')
			password = self.config.get('WEIBO-OAuth2','PASSWORD')
		except ConfigParser.NoOptionError:
		    print 'fetchNamePswd value is not found under section WEIBO-OAuth2 in ' + _PubVariable.infofile + '.'
		    raw_input('')
		    sys.exit(1)
		return name, password

	def fetchWbOauth2(self):
		try:
			appkey = self.config.get('WEIBO-OAuth2','APP_KEY')
			appsecret = self.config.get('WEIBO-OAuth2','APP_SECRET')
			classbackurl = self.config.get('WEIBO-OAuth2','CALLBACK_URL')
			authurl = self.config.get('WEIBO-OAuth2','AUTH_URL')
		except ConfigParser.NoOptionError:
			print 'fetchWbOauth2 value is not found under section WEIBO-OAuth2 in ' + _PubVariable.infofile + '.'
			sys.exit(1)
		return appkey,appsecret,classbackurl,authurl

	def fetchMysql(self):
		try:
			db = self.config.get('MYSQL-CONFIG','db')
			dbuser = self.config.get('MYSQL-CONFIG','db.user')
			dbpassword = self.config.get('MYSQL-CONFIG','db.password')
		except ConfigParser.NoOptionError, e:
			print 'fetchMysql value is not found under section MYSQL-CONFIG in ' + _PubVariable.infofile + '.'
			sys.exit(1)
		return db,dbuser,dbpassword
