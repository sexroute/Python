import time
import urllib
import urllib2
import cookielib
import base64
import re
import json
import rsa
import binascii

# proxy_hadler = urllib2.ProxyHandler({'http':'http://10.37.84.114:8080'})
# proxy_opener = urllib2.build_opener(proxy_hadler)
# urllib2.install_opener(proxy_opener)

cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
# opener = urllib2.build_opener(proxy_hadler,cookie_support,urllib2.HTTPHandler)
opener = urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
urllib2.install_opener(opener)


def prelogin(su):
    params = {
        'entry': 'weibo',
        'callback': 'sinaSSOController.preloginCallBack',
        'su': su,
        'rsakt': 'mod',
        'checkpin': '1',
        'client': 'ssologin.js(v1.4.18)',
        '_': str(time.time()*100)
    }
    url_prelogin = 'http://login.sina.com.cn/sso/prelogin.php'
    # r = requests.get(url_prelogin,params=params,proxies=proxies,headers=headers)

    data = re.search('\((.*)\)',urllib2.urlopen('%s?%s'%(url_prelogin,urllib.urlencode(params))).read()).group(1)
    tojson = json.loads(data)
    servertime = tojson.get('servertime')
    nonce = tojson.get('nonce')
    pubkey = tojson.get('pubkey')
    rsakv = tojson.get('rsakv')
    return servertime,nonce,pubkey,rsakv


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


def wb_login():
    su = encryname('1691234347@qq.com')
    servertime,nonce,pubkey,rsakv = prelogin(su)
    sp = encrypassword('00000a',servertime,nonce,pubkey)
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
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'
    }
    url_login = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'
    request = urllib2.Request(url_login,data=urllib.urlencode(postdata),headers=headers)
    
    url_final = re.search("location\.replace\(['|\"](.*?)['|\"]\)",urllib2.urlopen(request).read()).group(1)
    request = urllib2.Request(url_final,headers=headers)
    urllib2.urlopen(request)
    # print cj

    url_home = 'http://weibo.com/avnpc'
    # print urllib2.urlopen(url_home).read()
    # with open(r'D:\allo.html','w') as f:
    #     f.write(urllib2.urlopen(url_home).read())

if __name__ == '__main__':
    wb_login()



