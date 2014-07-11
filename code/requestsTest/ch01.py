__author__ = 'CHENGSIQIN754'

import requests

def myget():
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.get("http://httpbin.org/get", params = payload)
    print(r.url)

def mypost():
    r = requests.get('https://github.com/timeline.json')
    print(r.encoding)
    print(r.text)
    print(r.content)


if __name__ == '__main__':
    # myget()
    # mypost()
    pass
