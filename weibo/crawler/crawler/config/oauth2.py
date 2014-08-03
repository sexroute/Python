# -*- coding: utf-8 -*-
import urllib2
import urllib
from weibo import APIClient
from readconf import ReadConf
from keygen import Decryption
from abstract import ProcessAbstract

class _LocalVar:
	decry = Decryption()
	readConf = ReadConf()
	APP_KEY,APP_SECRET,CALLBACK_URL,AUTH_URL = readConf.fetchWbOauth2()
	name,password = ProcessAbstract.decryProcess(decry,readConf)

def getAccessToken():
    client = APIClient(app_key=_LocalVar.APP_KEY, app_secret=_LocalVar.APP_SECRET, redirect_uri=_LocalVar.CALLBACK_URL)
    referer_url = client.get_authorize_url()
    postdata = {
        "action": "login",
        "client_id": _LocalVar.APP_KEY,
        "redirect_uri":_LocalVar.CALLBACK_URL,
        "userId": _LocalVar.name,
        "passwd": _LocalVar.password,
        }

    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
        "Referer":referer_url,
        "Connection":"keep-alive"
    }

    req  = urllib2.Request(
        url = _LocalVar.AUTH_URL,
        data = urllib.urlencode(postdata),
        headers = headers
    )

    resp = urllib2.urlopen(req)
    code = resp.geturl()[-32:]
    r = client.request_access_token(code)
    access_token = r.access_token
    expires_in = r.expires_in
    urllib2.urlopen('http://weibo.com/u/2490013033').read().decode('gbk')
    return access_token

if __name__ == "__main__":
    getAccessToken()

