
import requests
import time
import json
import re
import base64
import urllib
import rsa
import binascii

# import sys
# reload(sys)
# sys.setdefaultencoding('UTF-8')


proxies = {
    'http': 'http://CHENGSIQIN754:77777Luxe@10.37.84.114:8080',
    'https': 'http://CHENGSIQIN754:77777Luxe@10.37.84.114:8080'
}

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'
}

def prelogin():
	params = {
		'entry': 'weibo',
		'callback': 'sinaSSOController.preloginCallBack',
		'su': 'xeoncode@gmail.cn',
		'rsakt': 'mod',
		'checkpin': '1',
		'client': 'ssologin.js(v1.4.18)',
		'_': str(time.time()*100)
	}
	url_prelogin = 'http://login.sina.com.cn/sso/prelogin.php'
	r = requests.get(url_prelogin,params=params,proxies=proxies,headers=headers)
	# url_prelogin = "http://login.sina.com.cn/sso/prelogin.php&client=ssologin.js(v1.4.18)&_=%s" % str(time.time())
	# print r.url
	data = re.search('\((.*)\)',r.text).group(1)
	tojson = json.loads(data)
	servertime = tojson.get('servertime')
	nonce = tojson.get('nonce')
	pubkey = tojson.get('pubkey')
	rsakv = tojson.get('rsakv')
	return servertime,nonce,pubkey,rsakv
	# print r.cookies

def encryname(name):
	name = urllib.quote(name)
	return base64.encodestring(name)[:-1]

def encrypassword(password,servertime,nonce,pubkey):
	rsaPublickey = int(pubkey,16)
	key = rsa.PublicKey(rsaPublickey,65537)
	message = str(servertime)+'\t'+str(nonce)+'\n'+str(password)
	password = rsa.encrypt(message,key)
	password = binascii.b2a_hex(password)
	return password



servertime,nonce,pubkey,rsakv = prelogin()
su = encryname('@gmail.com')
# print encryname('@gmail.com')
sp = encrypassword('',servertime,nonce,pubkey)

postdata = {
	'entry': 'weibo',
	'gateway': '1',
	'from': '',
	'savestate': '7',
	'useticket':'1',
	'vsnf': '1',
	'su': su,
	'service': 'miniblog',
	'servertime': servertime,
	'nonce': nonce,
	'pwencode': 'rsa2',
	'rsakv': rsakv,
	'sp': sp,
	'encoding': 'UTF-8',
	'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
	'returntype': 'META'
}

s = requests.Session()
url_login = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'
r = s.post(url_login,data=postdata,proxies=proxies,headers=headers)
# print r.content
# print s.cookies


url_final = re.search("location\.replace\('(.*?)'\)",r.content).group(1)
r = s.get(url_final,proxies=proxies,headers=headers)
# print s.cookies


url_home = 'http://weibo.com/u/2490013033'
r = s.get(url_home,proxies=proxies,headers=headers)
# print r.content

with open(r'D:\wb.html','w') as f:
	f.write(r.content)
