from os import stat,fstat
import time
statinfo = stat(r"D:\somefile.txt")
# print statinfo.st_size
# print statinfo.st_mtime
# print time.time()

print time.time()-statinfo.st_mtime
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


import ConfigParser

