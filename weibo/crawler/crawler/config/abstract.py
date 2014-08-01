import sys
import ConfigParser
import re

def infoinput():
	name = raw_input("Please input UM: ").strip()
	passwd = raw_input("Please input UM password: ").strip()
	if name.find(' ')!=-1 or passwd.find(' ')!=-1:
		print "can't contain whitespace!".title()
		sys.exit(1)
	return name,passwd


class _PubVariable(object):
	"""docstring for _PubVariable"""
	infofile = "info.conf"


class EncryAbstract(object):
	"""docstring for EncryAbstract"""
	def encodeValue(self,value,reverse=False):
		pass
	def outputValue(self,name,password):
		""" writing encrypted name&password to config file """
		with open(_PubVariable.infofile,'r+') as f:
			content = f.read()
			content = re.sub('USER_NAME =.*', 'USER_NAME = '+name, content)
			content = re.sub('PASSWORD =.*','PASSWORD = '+password, content)
			f.seek(0)
			f.write(content)


class DecryAbstract(object):
	"""docstring for DecryAbstract"""
	def __init__(self):
		super(DecryAbstract, self).__init__()
	def decodeValue(self,value,reverse=False):
		pass


class ReadConfAbstract(object):
	"""docstring for ReadConfAbstract"""
	def __init__(self):
		super(ReadConfAbstract, self).__init__()
		# self.config = None
		self.config = None
		self.__getConf()

	def __getConf(self):
		if self.config != None:
			return self.config
		try:
		    configFile = open(_PubVariable.infofile, "r")
		except IOError:
		    print _PubVariable.infofile + ' is not found'
		    sys.exit(1)
		self.config = ConfigParser.ConfigParser()
		self.config.readfp(configFile)
		configFile.close()

	def fetchNamePswd(self):
		pass


class ProcessAbstract:
	"""docstring for ProcessAbstract"""
	@staticmethod
	def encryProcess(encry,name='',password=''):
		"""encry is a instance of subclass of EncryAbstract """
		if name.strip == '' or password.strip() == '':
			name,password = infoinput()
		name = encry.encodeValue(name)
		password = encry.encodeValue(password,True)
		encry.outputValue(name,password)

	@staticmethod
	def decryProcess(decry,readconf,name=None,password=None):
		""" decry is a instance of subclass of DecryAbstract """
		if name==None or password==None:
			name,password = readconf.fetchNamePswd()
		return decry.decodeValue(name), decry.decodeValue(password,True)


