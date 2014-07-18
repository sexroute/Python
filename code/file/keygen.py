import sys,random,os,re,ConfigParser
from abstract import *


class _PubVariable(object):
	"""docstring for _PubVariable"""
	RandomRange = 128
	SaltStart = 14
	SaltEnd = 24
	pubkeyfile = ".pubkey.key"
	infofile = "info.conf"
	filelistfile = "filelist.list"


class Encryption(EncryAbstract):
	"""docstring for Encryption"""
	def __init__(self):
		super(Encryption,self).__init__()
		self.keymap = []

	def _mapgen(self):
		""" generate random mapping list """
		if self.keymap != []:
			return self.keymap
		for x in range(0,_PubVariable.RandomRange):
			self.keymap.append(random.randint(0,94))
		return self.keymap

	def encodeValue(self,value,reverse=False):
		""" encrypt string with random mapping list generated by mapgen() """
		keymap = self._mapgen()
		encryValue = ''
		if len(value)<33:
			for x in range(0,len(value)):
				encryValue += chr(( ord(value[x]) - 33 + (lambda x : keymap[_PubVariable.RandomRange-1-x] if reverse else keymap[x])(x) )%95 + 33) # lambda can be replace by (keymap[_PubVariable.RandomRange-1-x] if reverse else keymap[x])
			encryValue += chr(random.randint(_PubVariable.SaltStart,_PubVariable.SaltEnd))
			for x in xrange(len(value)+1,32):
				# encryValue += chr((keymap[_PubVariable.RandomRange-1-x] if reverse else keymap[x]) + 33)
				encryValue += chr( (range(_PubVariable.SaltStart,_PubVariable.SaltEnd+1)+range(33,128))[random.randint(0,105)] )
		elif len(value)<=_PubVariable.RandomRange:
			for x in xrange(0,len(value)):
				encryValue += chr(( ord(value[x]) - 33+ (keymap[_PubVariable.RandomRange-1-x] if reverse else keymap[x]) )%95 + 33)
		else:
			print 'your value is so long!'.title()
			sys.exit(1)
		return encryValue

	def _addSalt(self):
		""" add random salt to keymap generated by mapgen() """
		addsalt = self._mapgen()[:]
		for x in xrange(0,10):
			salt = random.randint(_PubVariable.SaltStart,_PubVariable.SaltEnd) - 33
			addsalt.insert(random.randint(0,len(addsalt)),salt)
		return ''.join(chr(i + 33) for i in addsalt)

	def writepubkey(self):
		""" store the pubkey value """
		pubkey = self._addSalt()
		if os.path.exists(_PubVariable.pubkeyfile):
			os.system('attrib -S -H -R ' + _PubVariable.pubkeyfile)
		with open(_PubVariable.pubkeyfile, "w") as f:
			f.write(pubkey)
		os.system(r'attrib +S +H +R ' + _PubVariable.pubkeyfile)

	def writeConf(self,name,password):
		""" writing encrypted name&password to config file """
		with open(_PubVariable.infofile,'w') as conf, open(_PubVariable.filelistfile,'w') as ls:
			conf.writelines(
				"""[HADOOP-SVN-INFO]
baseurl  = http://svn.paic.com.cn/svn/pad_hadoop/trunk
username = %s
password = %s
fileList = fileList.list"""%(name,password))
			ls.write("src/main/resources/config/Pad-dbw/pad-common/datasets.xml")


class ReadConf(object):
	"""docstring for ReadConf"""
	def __init__(self):
		super(ReadConf, self).__init__()
		self.config = None

	def _getConf(self):
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

	def fetchNamePsd(self):
		config = self._getConf()
		try:
			name = config.get('HADOOP-SVN-INFO','username')
			password = config.get('HADOOP-SVN-INFO','password')
		except ConfigParser.NoOptionError:
		    print 'value is not found under section HADOOP-SVN-INFO in ' + _PubVariable.infofile + '.'
		    raw_input('')
		    sys.exit()
		return name, password

	def fetchBaseUrl(self):
		config = self._getConf()
		try:
			baseurl = config.get('HADOOP-SVN-INFO','baseurl')
			baseurl = baseurl.rstrip('/')
		except ConfigParser.NoOptionError:
			print 'value is not found under section HADOOP-SVN-INFO in ' + _PubVariable.infofile + '.'
			sys.exit()
		return baseurl

	def fetchFileList(self):
		config = self._getConf()
		try:
			fileList = config.get('HADOOP-SVN-INFO','fileList')
		except ConfigParser.NoOptionError:
			print 'value is not found under section HADOOP-SVN-INFO in ' + _PubVariable.infofile + '.'
			sys.exit()
		with open(fileList, "r") as ls:
			fileList = ls.readlines()
		return fileList



class Decryption(DecryAbstract):
	"""docstring for Decryption"""
	salt = '['+''.join([chr(x) for x in range(_PubVariable.SaltStart,_PubVariable.SaltEnd+1)]) + ']'
	keymap = []
	def _clearKey(self):
		""" clear salt in pubkey written by Encryption.writepubkey() """
		if self.keymap != []:
			return self.keymap
		with open(_PubVariable.pubkeyfile, "r") as f:
			self.keymap = f.read()
		self.keymap = re.sub(self.salt, '', self.keymap)
		return self.keymap

	def decodeValue(self,value,reverse=False):
		keymap = self._clearKey()
		decryValue = ''
		value = re.sub(self.salt+".*", '', value)
		if len(value)<=_PubVariable.RandomRange:
			for x in xrange(0,len(value)):
				decryValue += chr( (ord(value[x]) - ord(keymap[_PubVariable.RandomRange-1-x] if reverse else keymap[x]) )%95 +33 )
		else:
			print "value is so long! cut it please!".title()
			sys.exit(1)
		return decryValue



class ProcessDeal(ProcessAbstract):
	"""docstring for Process"""
	@staticmethod
	def encryProcess(encry,name='',password=''):
		"""encry is a instance of subclass of EncryAbstract """
		if name.strip == '' or password.strip() == '':
			name,password = infoinput()
		name = encry.encodeValue(name)
		password = encry.encodeValue(password,True)
		encry.writepubkey()
		encry.writeConf(name,password)

	@staticmethod
	def decryProcess(decry,readconf,name=None,password=None):
		""" decry is a instance of subclass of DecryAbstract """
		if name==None or password==None:
			name,password = readconf.fetchNamePsd()
		return decry.decodeValue(name), decry.decodeValue(password,True)


if __name__ == '__main__':
	ProcessDeal.encryProcess(Encryption())




# =================== encryption process
# encry = Encryption()
# encryKey = encry._mapgen()
# name, password = infoinput()
# print encry.encodeValue("CHENGSIQIN754",encryKey)
# print encry.encodeValue("Loveyou",encryKey,True)
# encry.writeConf( encry.encodeValue(name, encryKey), encry.encodeValue(password, encryKey, True) )
# encry.writepubkey(encry.addSalt(encryKey))


# value = [1,2]
# value02 = [3,4]
# print value + value02


# =================== decryption process
# decry = Decryption()
# print decry.decodeValue("""lR%qh)8wc-F[>x/'SUyvc6$svui~`e3""")
# print decry.decodeValue("""5ArYO{Fp_Dq}iDzcH<n5NB@r[rtuZhf""",True)
# print -1%95

# ===================
# reg = '['+''.join([chr(x) for x in range(_PubVariable.SaltStart,_PubVariable.SaltEnd+1)]) + '].*'
# salt = re.compile( '[' +''.join([chr(x) for x in range(_PubVariable.SaltStart,_PubVariable.SaltEnd+1)])+"].*" )
# salt = re.compile( reg )
# print reg
# value = """gn/\Oy"y&Xy^RCv3-_&%u%+6P:3SY(Z_L-Iba^^SLQ!^&3n;v?#(#y\`iTKJxI$Rb;FI_D*3SX3@i=uK[db|j0}<1%>-sNRjXbs007F`OvsGp}d{s>)Dyx)wUJ(fo84"""
# value = """JVsJ6ljjnF0rev3-_&%u%+6P:3SY(Z_"""
# print re.sub(reg, '', value)
# print m.group()



# encry = Encryption()
# encryKey = encry.mapgen()
# encryValue01 = encry.encodeValue('CHENGSIQIN754', encryKey)
# encryValue02 = encry.encodeValue('passwordofmine', encryKey, True)
# print encryValue.index(chr(1))
# print encryValue01[:encryValue01.find(chr(1))]
# print encryValue02[:encryValue02.find(chr(1))]
# encry.writeConf(encryValue01,encryValue02)


# print encryKey
# print len(encryKey)
# print [chr(i+32) for i in encryKey]
# print ''.join(chr(i) for i in encryKey)
# print encry.addSalt(encryKey)
# writepubkey(encry.addSalt(encryKey))


# print decry.clearKey()
# print repr(clearKey())
# print len(decry.clearKey())



# value = 'CHENGSIQIN754'
# print ord(value[0])

# print [value[x] for x in range(0,len(value))]

# print mapgen()[:32]

# print [chr(x) for x in xrange(33,127)]
# print [chr(x) for x in xrange(0,256)]
# print [ord(chr(x)) for x in xrange(0,256)]
# print [chr(x) for x in range(14,32)]
# print '|'.join([chr(x) for x in range(14,32)])
# print [chr(x) for x in range(33,127)]


# saltValue = addSalt(encryKey)
# print saltValue
# pattern = re.compile('|'.join([chr(x) for x in range(14,32)]))
# print pattern.sub('', saltValue)
# print saltValue


# with open("./test.key","w") as w:
# 	w.write('M'.join([chr(x) for x in range(14,24)]))
# with open("./test.key", "r") as f:
# 	keyMap = f.read()
# with open("./pubkey.key", "r") as f:
# 	keyMap02 = f.read()
# print repr(keyMap)
# print repr(keyMap02)

