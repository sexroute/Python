__author__ = 'CHENGSIQIN754'

import requests

def myget():
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get("http://httpbin.org/get", params = payload)
    print(r.url)

def mypost():
    r = requests.get('https://github.com/timeline.json')
    return r,r.text, r.content, r.encoding

def myimage():
	from PIL import Image
	from StringIO import StringIO
	i = Image.open(StringIO(r.content))

def myjson():
	# print(mypost()[1])
	# print(mypost()[0].json())
	print(mypost()[0].headers)




if __name__ == '__main__':
    # myget()
    # mypost()
    # myimage()
    myjson()
    pass

