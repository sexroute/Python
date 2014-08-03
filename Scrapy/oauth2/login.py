import urllib2
import urllib

postdata = {
        "entry": "weibo",
        "url": "http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack",
        "username": "siq.unix@gmail.com",
        "password": "2012Wb",
        }

headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
    "Referer":"http://weibo.com/",
    "Connection":"keep-alive"
}

from cookielib import CookieJar
cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

req  = urllib2.Request(
    url = "http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)",
    data = urllib.urlencode(postdata),
    headers = headers
)

# opener.open(req)
# print opener.open('http://weibo.com/u/2490013033').read().decode('gbk')

resp = urllib2.urlopen(req)
print urllib2.urlopen('http://weibo.com/u/2490013033').read().decode('gbk')

for index,cookie in enumerate(cj):
    print '[',index,']',cookie
# print resp.read().decode('gbk')
# print resp.geturl()

