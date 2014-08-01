from keygen import *
from ReadConf import *

class _LocalVar:
    decry = Decryption()
    readConf = ReadConf()
    appkey,appsecret,classbackurl = readConf.fetchWbOauth2()
    db,dbuser,dbpassword = readConf.fetchMysql()
    name,password = ProcessAbstract.decryProcess(decry,readConf)

decry = Decryption()
readConf = ReadConf()
# print readConf.fetchWbOauth2()
# print readConf.fetchMysql()
# print ProcessAbstract.decryProcess(decry,readConf)