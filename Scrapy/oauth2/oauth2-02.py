# coding=utf-8
from weibo import APIClient
import webbrowser

APP_KEY = '3515759340'
APP_SECRET = 'aa0be2ca13abc063741126b32401b9e8'
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'
client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()

# code = your.web.framework.request.get('code')
print url
# webbrowser.open_new(url)
code = raw_input()

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
r = client.request_access_token(code)
access_token = r.access_token
expires_in = r.expires_in
print access_token, expires_in
client.set_access_token(access_token, expires_in)

# statuses = client.statuses.user_timeline.get()
# print statuses['statuses']
# for x in range(0,len(statuses['statuses'])):
# 	print u'昵称: ' + statuses['statuses'][x]['user']['screen_name']
# 	print u'简介：'+statuses['statuses'][x]['user']['description']
# 	print u'位置：'+statuses['statuses'][x]['user']['location']
# 	print u'微博：'+statuses['statuses'][x]['text']

# print client.statuses.update.post(status=u'test')
# print client.statuses.upload.post(status=u'test2', pic=open('18.jpg'))

r = client.statuses.user_timeline.get(uid=2490013033)
for st in r.statuses:
    print st.text

