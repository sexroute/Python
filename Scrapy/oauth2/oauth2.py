from weibo import APIClient
import urllib2
import urllib

APP_KEY = '3515759340'
APP_SECRET = 'aa0be2ca13abc063741126b32401b9e8'
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'
AUTH_URL = 'https://api.weibo.com/oauth2/authorize'

def GetCode(userid,passwd):
    client = APIClient(app_key = APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    referer_url = client.get_authorize_url()
    postdata = {
        "action": "login",
        "client_id": APP_KEY,
        "redirect_uri":CALLBACK_URL,
        "userId": userid,
        "passwd": passwd,
        }

    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
        "Referer":referer_url,
        "Connection":"keep-alive"
    }
    req  = urllib2.Request(
        url = AUTH_URL,
        data = urllib.urlencode(postdata),
        headers = headers
    )
    resp = urllib2.urlopen(req)
    print resp.read()
    return resp.geturl()[-32:]
if __name__ == "__main__":
    print GetCode('SiQ.Unix@gmail.com','2012Wb')

