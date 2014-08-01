# -*- coding: utf-8 -*-

from weibo import APIClient
from readconf import ReadConf
from keygen import Decryption
from abstract import ProcessAbstract

class _LocalVar:
	decry = Decryption()
	readConf = ReadConf()
	APP_KEY,APP_SECRET,CALLBACK_URL,AUTH_URL = readConf.fetchWbOauth2()
	name,password = ProcessAbstract.decryProcess(decry,readConf)


print (_LocalVar.APP_KEY,_LocalVar.APP_SECRET,_LocalVar.CALLBACK_URL,_LocalVar.AUTH_URL)
print (_LocalVar.name,_LocalVar.password)

# APP_KEY = '3515759340'
# APP_SECRET = 'aa0be2ca13abc063741126b32401b9e8'
# CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'


def getAccessToken(userid,passwd):
    client = APIClient(app_key=_LocalVar.APP_KEY, app_secret=_LocalVar.APP_SECRET, redirect_uri=_LocalVar.CALLBACK_URL)
    referer_url = client.get_authorize_url()
    postdata = {
        "action": "login",
        "client_id": APP_KEY,
        "redirect_uri":CALLBACK_URL,
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
    client.request_access_token(code)
    access_token = r.access_token
    expires_in = r.expires_in
    return access_token

if __name__ == "__main__":
    pass








