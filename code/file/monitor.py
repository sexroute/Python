from os import stat,fstat
import time
statinfo = stat(r"D:\somefile.txt")
# print statinfo.st_size
# print statinfo.st_mtime
# print time.time()

# print time.time()-statinfo.st_mtime
# print time.localtime(statinfo.st_mtime)
# print time.strftime('%Y/%m/%d %H:%M', time.localtime(statinfo.st_mtime))

if time.time()-statinfo.st_mtime<300:
	print 'need to check'

with open(r"D:\index.dat", "wb") as index:
	index.write(str(statinfo.st_mtime))

# 1. svn reading, http/local file
# 2. modify time compare
# 3. text analysis 
# 4. product report 


import sys
import ConfigParser
try:
    configFile = open("info.conf", "r")
except IOError:
    print 'info.conf is not found'
    raw_input('')
    sys.exit()

config = ConfigParser.ConfigParser()
config.readfp(configFile)
configFile.close()

try:
    baseurl = config.get('INFO','baseurl')
    baseurl = baseurl.rstrip('/')
    baseurl = '%s/'%baseurl
except ConfigParser.NoOptionError:
    print 'baseurl is not found under section INFO in info.conf.'
    raw_input('')
    sys.exit()

import urllib2
realm = "CollabNet Subversion Repository"
auth = urllib2.HTTPBasicAuthHandler()
auth.add_password(realm, baseurl, 'CHENGSIQIN754', 'Qin2012Luxe')
opener = urllib2.build_opener(auth, urllib2.CacheFTPHandler)
urllib2.install_opener(opener)

url = '%s%s'%(baseurl,'/src/main/resources/config/Pad-dbw/pad-common/datasets.xml')
data = urllib2.urlopen(url)
data.read()
# print data.read()


import urllib2
import sys
req = urllib2.Request('http://svn.paic.com.cn/svn/pad_hadoop/trunk')
try:
    handle = urllib2.urlopen(req)
    print 'open again is ok'
except IOError, e:
    print "can't open it"
    pass
else:
    print "This page isn't protected by authentication."
    sys.exit(1)
getrealm = e.headers['www-authenticate']
print getrealm



