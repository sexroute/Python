import sys
def infoinput():
	name = raw_input("Please input UM: ").strip()
	passwd = raw_input("Please input UM password: ").strip()
	if name.find(' ') or passwd.find(' '):
		print "can't contain whitespace!".title()
		sys.exit(1)
	return name,passwd

import random, os
RandomRange = 128
def mapgen():
	keymap = []
	for x in range(0,RandomRange):
		keymap.append(random.randint(0,94))
	return keymap

def addSalt(keymap):
	addsalt = keymap[:]
	for x in xrange(0,10):
		salt = random.randint(14,31) - 32
		addsalt.insert(random.randint(0,len(keymap)),salt)
	return ''.join(chr(i + 32) for i in addsalt)

def writepubkey(pubkey):
	if os.path.exists(r'pubkey.key'):
		os.system(r'attrib -H pubkey.key')
	with open("./pubkey.key", "w") as f:
		f.write(pubkey)
	os.system(r'attrib +H pubkey.key')

def clearKey(pubkey):
	pass



def encodeValue(value,keymap,reverse=False):
	encryValue = ''
	if len(value)<33:
		for x in range(0,len(value)):
			encryValue += chr(( ord(value[x]) - 33 + (lambda x : keymap[RandomRange-1-x] if reverse else keymap[x])(x) )%95 + 33) # lambda can be replace by (keymap[RandomRange-1-x] if reverse else keymap[x])
		encryValue += chr(1)
		for x in xrange(len(value)+1,32):
			encryValue += chr(keymap[x] + 33)
	elif len(value)<=RandomRange:
		for x in xrange(1,len(value)):
			encryValue += chr(( ord(value[x]) - 33+ (keymap[RandomRange-1-x] if reverse else keymap[x]) )%95 + 33)
	else:
		print 'your value is so long!'.title()
	return encryValue

def writeConf(name, password):
	with open('./info.conf-bak','w') as conf:
		conf.writelines(
			"""[HADOOP-SVN-INFO]
baseurl  = http://svn.paic.com.cn/svn/pad_hadoop/trunk
user     = %s
password = %s
fileList = fileList.list
"""%(name,password))









encryKey = mapgen()
encryValue01 = encodeValue('CHENGSIQIN754', encryKey)
encryValue02 = encodeValue('password', encryKey, True)
# print encryValue.index(chr(1))
# print encryValue01[:encryValue01.find(chr(1))]
# print encryValue02[:encryValue02.find(chr(1))]
writeConf(encryValue01,encryValue02)


# print encryKey
# print len(encryKey)
# print [chr(i+32) for i in encryKey]
# print ''.join(chr(i) for i in encryKey)
# print addSalt(encryKey)
writepubkey(addSalt(encryKey))


# value = 'CHENGSIQIN754'
# print ord(value[0])

# print [value[x] for x in range(0,len(value))]

# print mapgen()[:32]

# print [chr(x) for x in xrange(33,127)]
# print [chr(x) for x in xrange(0,256)]
