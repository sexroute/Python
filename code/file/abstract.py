
def infoinput():
	name = raw_input("Please input UM: ").strip()
	passwd = raw_input("Please input UM password: ").strip()
	if name.find(' ')!=-1 or passwd.find(' ')!=-1:
		print "can't contain whitespace!".title()
		sys.exit(1)
	return name,passwd
		

class EncryAbstract(object):
	"""docstring for EncryAbstract"""
	# def __init__(self):
	# 	super(EncryAbstract, self).__init__()
	def encodeValue(self,value,reverse=False):
		pass
	def writeConf(self,name,password):
		pass

class ReadConfAbstract(object):
	"""docstring for ReadConfAbstract"""
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











