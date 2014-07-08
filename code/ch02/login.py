"""Login module
Interface summary:
	details
"""
import sys,urllib
from http import cookiejar
class Login:
	"""docstring for Login
	"""
	def __init__(self, arg=None):
		super(Login, self).__init__()
		self.arg = arg
	cookiejar.LWPCookieJar()


