__author__ = 'CHENGSIQIN754'
from urllib import request
import sys
def myurl():
    f = request.urlopen('http://www.baidu.com/')
    print(f.read().decode('utf-8'))

def myssl():
    req = request.Request(url='https://localhost/cgi-bin/test.cgi',data=b'This data is passed to stdin of the CGI')
    f = request.urlopen(req)
    print(f.read().decode('utf-8'))

def myput():
    DATA = b'some data'
    req = request.Request(url='http://localhost:8080', data=DATA, method='PUT')
    f = request.urlopen(req)
    print(f.status)
    print(f.reason)

def myopener():
    auth_handler = request.HTTPBasicAuthHandler()
    auth_handler.add_password(realm='PDQ Application',
                              uri='https://mahler:8092/site-updates.py',
                              user='klem',
                              passwd='kadidd!ehopper')
    opener = request.build_opener(auth_handler)
    request.install_opener(opener)
    request.urlopen('http://www.example.com/login.html')

def myagent():
    opener = request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    opener.open('http://pip.readthedocs.org/en/latest/installing.html')


from urllib import parse
def myparse():
    params = parse.urlencode({'span':1, 'eggs':2, 'bacon':0})
    params = params.encode('utf-8')
    # f = request.urlopen("http://www.musi-cal.com/cgi-bin/query?%s" % params)
    # print(f.read().decode('utf-8'))
    req = request.Request("http://requestb.in/xrbl82xr")
    req.add_header("Content-Type", "application/x-www-form-urlencoded;charset=utf-8")
    f = request.urlopen(req, params)
    print(f.read().decode('utf-8'))

def myhttpproxy():
    proxies = {'http':'10.37.84.114:8080'}
    opener = request.FancyURLopener(proxies)
    f = opener.open("http://www.python.org")
    print(f.read().decode('utf-8'))

from http import client
def myhttpclient():
    params = parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
    headers = {"Content-type": "application/x-www-form-urlencoded",
               "Accept": "text/plain"}
    conn = client.HTTPConnection("bugs.python.org")
    conn.request("POST", "", params, headers)
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read()
    print(data)
    conn.close()





# myurl()
# myssl()
# myput() version 3.4
# myopener()
# myagent()
# myparse()
# myhttpproxy()
# myhttpclient()








