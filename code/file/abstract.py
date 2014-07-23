
def infoinput():
	name = raw_input("Please input UM: ").strip()
	passwd = raw_input("Please input UM password: ").strip()
	if name.find(' ')!=-1 or passwd.find(' ')!=-1:
		print "can't contain whitespace!".title()
		sys.exit(1)
	return name,passwd
		

import ConfigParser

class _PubVariable(object):
	"""docstring for _PubVariable"""
	infofile = "info.conf"
	filelistfile = "filelist.list"


class EncryAbstract(object):
	"""docstring for EncryAbstract"""
	def encodeValue(self,value,reverse=False):
		pass
	def writeConf(self,name,password):
		""" writing encrypted name&password to config file """
		# self._writepubkey()
		with open(_PubVariable.infofile,'w') as conf, open(_PubVariable.filelistfile,'w') as ls:
			conf.writelines(
				"""[HADOOP-SVN-INFO]
baseurl  = http://svn.paic.com.cn/svn/pad_hadoop/trunk
username = %s
password = %s
fileList = fileList.list"""%(name,password))
			ls.write("src/main/resources/config/Pad-dbw/pad-common/datasets.xml")


class ReadConfAbstract(object):
	"""docstring for ReadConfAbstract"""
	def __init__(self):
		super(ReadConfAbstract, self).__init__()
		self.config = None

	def getConf(self):
		if self.config != None:
			return config
		try:
		    configFile = open(_PubVariable.infofile, "r")
		except IOError:
		    print _PubVariable.infofile + ' is not found'
		    sys.exit(1)
		config = ConfigParser.ConfigParser()
		config.readfp(configFile)
		configFile.close()
		return config

	def fetchNamePswd(self):
		pass


class DecryAbstract(object):
	"""docstring for DecryAbstract"""
	def __init__(self):
		super(DecryAbstract, self).__init__()
	def decodeValue(self,value,reverse=False):
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
		encry.writeConf(name,password)

	@staticmethod
	def decryProcess(decry,readconf,name=None,password=None):
		""" decry is a instance of subclass of DecryAbstract """
		if name==None or password==None:
			name,password = readconf.fetchNamePswd()
		return decry.decodeValue(name), decry.decodeValue(password,True)











