from keygen import ReadConf,ProcessDeal,Decryption,Encryption
from xml.dom.minidom import parseString, parse
import urllib2,re
import pprint


class _LocalVar:
    decry = Decryption()
    readConf = ReadConf()
    baseurl = readConf.fetchBaseUrl()
    fileList = readConf.fetchFileList()
    name,password = ProcessDeal.decryProcess(decry,readConf)

class SvnRead(object):
    """docstring for SvnRead"""
    def __init__(self):
        super(SvnRead,self).__init__()

    def _fetchRealm(self):
        req = urllib2.Request(_LocalVar.baseurl)
        try:
            handle = urllib2.urlopen(req)
        except IOError as e:
            return re.search('\"(.+)\"',e.headers['www-authenticate']).group(0).strip('"')
        else:
            return None

    def _fetchFile(self,svnfile):
        realm = self._fetchRealm()
        auth = urllib2.HTTPBasicAuthHandler()
        auth.add_password(realm,_LocalVar.baseurl,_LocalVar.name,_LocalVar.password)
        opener = urllib2.build_opener(auth, urllib2.CacheFTPHandler)
        urllib2.install_opener(opener)
        url = '%s/%s'%(_LocalVar.baseurl,svnfile)
        data = urllib2.urlopen(url)
        return data.read()

    def report(self,tag,attrib):
        names = []
        for line in _LocalVar.fileList:
            if line=="":
                pass
            else:
                dom = parseString(self._fetchFile(line))
                datasets = dom.getElementsByTagName(tag)
                for dataset in datasets:
                    names.append(str(dataset.getAttribute(attrib)))
        return [(names[i],i) for i in range(len(names)) if names.count(names[i])>1]


svnRead = SvnRead()
print svnRead.report("datasets","name")





# data = readData()
# print data

# dom = parseString(data)
# dom = parse(r"D:\datasets.xml")
# datasets = dom.getElementsByTagName("dataset")
# names = []
# for dataset in datasets:
#     names.append(str(dataset.getAttribute("name")))
# print [(names[i],i) for i in range(len(names)) if names.count(names[i])>1]
# print len(names)
# print names
# print [i for i in range(len(names))]



# value = "CollabNet Subversion Repository"
# print value

# from os import stat,fstat
# import time
# statinfo = stat(r"D:\somefile.txt")
# print statinfo.st_size
# print statinfo.st_mtime
# print time.time()

# print time.time()-statinfo.st_mtime
# print time.localtime(statinfo.st_mtime)
# print time.strftime('%Y/%m/%d %H:%M', time.localtime(statinfo.st_mtime))

# if time.time()-statinfo.st_mtime<300:
#     print 'need to check'
# with open(r"D:\index.dat", "wb") as index:
#     index.write(str(statinfo.st_mtime))

# 1. svn reading, http/local file
# 2. modify time compare
# 3. text analysis 
# 4. product report 