import urllib2
import urllib

postdata = {
        "entry": "weibo",
        "url": "http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack",
        "username": "",
        "password": "",
        }

headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36",
    "Referer":"http://weibo.com/",
    "Connection":"keep-alive"
}
req  = urllib2.Request(
    url = "http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)",
    data = urllib.urlencode(postdata),
    headers = headers
)
resp = urllib2.urlopen(req)
print resp.read().decode('gbk')
print resp.geturl()
