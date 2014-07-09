"""Login module
Interface summary:
	details
"""
import pdb

from pprint import pprint
from urllib import request
from urllib import parse
from http import cookiejar
import json, rsa, base64, re, binascii, hashlib
try:
	import sys
except ImportError:
	_have_sys = False
else:
	_have_sys = True

class Login:
	"""docstring for Login
	"""
	def __init__(self, arg=None):
		super(Login, self).__init__()
		self.arg = arg
	cookie = cookiejar.LWPCookieJar()
	cookie_support = request.HTTPCookieProcessor(cookie)
	opener = request.build_opener(cookie_support, request.HTTPHandler)
	request.install_opener(opener)
	postdata = {
		'entry': 'weibo',  
        'gateway': '1',  
        'from': '',  
        'savestate': '7',  
        'userticket': '1',  
        'ssosimplelogin': '1',  
        'vsnf': '1',  
        'vsnval': '',  
        'su': '',  
        'service': 'miniblog',  
        'servertime': '',  
        'nonce': '',  
        'pwencode': 'rsa2',  
        'sp': '',  
        'encoding': 'UTF-8',  
        'prelt': '115',  
        'rsakv': '', 
        'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',  
        'returntype': 'META'
	}

	def get_servertime(self, username):
		"""
		summary: 
			encoding format in text
		"""
		url = 'http://login.sina.com.cn/sso/prelogin.php?entry=sso&callback=sinaSSOController.preloginCallBack&su=%s&rsakt=mod&client=ssologin.js(v1.4.4)' % username
		data = request.urlopen(url).read().decode('ASCII')
		p = re.compile('\((.*)\)')
		try:
			json_data = p.search(data).group(1)
			data = json.loads(json_data)
			servertime = str(data['servertime'])
			nonce = data['nonce']
			pubkey = data['pubkey']
			rsakv = data['rsakv']
			return servertime, nonce, pubkey, rsakv
		except:
			print('Get servertime error')
			return None

	def get_pwd(self, password, servertime, nonce, pubkey):
		rsaPublickey = int(pubkey, 16)
		key = rsa.PublicKey(rsaPublickey, 65537)
		message = str(servertime) + '\t' + str(nonce) + '\n' + str(password)
		passwd = rsa.encrypt(message.encode('ascii'), key)
		passwd = binascii.b2a_hex(passwd)
		return passwd

	def get_user(self, username):
		username_ = parse.quote(username)
		username = base64.encodestring(username_.encode('ascii'))[:-1]
		print("username: " + username.decode('ascii'))
		return username

	def get_account(self, filename):
		f = open(filename)
		flag = 0
		for line in f:
			if flag == 0:
				username = line.strip()
				flag += 1
			else:
				pwd = line.strip()
		f.close()
		return username, pwd

	def login(self, filename):
		# pdb.set_trace()
		username, pwd = self.get_account(filename)
		url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.4)'
		try:
			servertime, nonce, pubkey, rsakv = self.get_servertime(username)
			print(servertime)
			print(nonce)
			print(pubkey)
			print(rsakv)
		except:
			print('get servertime error')
			return
		Login.postdata['servertime'] = servertime
		Login.postdata['nonce'] = nonce
		Login.postdata['rsakv'] = rsakv
		Login.postdata['su'] = self.get_user(username)
		Login.postdata['sp'] = self.get_pwd(pwd, servertime, nonce, pubkey)
		Login.postdata = parse.urlencode(Login.postdata)
		headers = {'User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0 Chrome/20.0.1132.57 Safari/536.11'}
		req = request.Request(url = url, data = Login.postdata.encode('ascii'), headers = headers)
		result = request.urlopen(req)
		text = result.read().decode('GBK')
		# print(text.encode('GBK'))
		p = re.compile('location\.replace\(\"(.*)\"\)')
		try:
			login_url = p.search(text).group(1)
			print(login_url)
			print("Login success!")
			return 1
		except:
			print('Login error')
			return 0


if __name__ == '__main__':
	filename = './config/account'
	wbLogin = Login()
	if wbLogin.login(filename)==1:
		print('Main Login success!')
	else:
		print('Main Login error!')
		exit()

