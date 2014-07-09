import login
from urllib import request
import time

filename = './config/account'
wbLogin = login.Login()
if wbLogin.login(filename)==1:
	print('Login success!')
else:
	print('Main Login error!')
	exit()