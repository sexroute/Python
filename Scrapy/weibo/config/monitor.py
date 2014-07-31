from keygen import ReadConf,ProcessAbstract,Decryption,Encryption
from xml.dom.minidom import parseString, parse
import urllib2,re
import pprint


class _LocalVar:
    decry = Decryption()
    readConf = ReadConf()
    
    name,password = ProcessAbstract.decryProcess(decry,readConf)

print _LocalVar.name
print _LocalVar.password


