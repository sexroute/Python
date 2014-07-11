from urllib import request
from urllib import parse
from http import cookiejar

import requests
from pprint import pprint

class Myrequest(object):
        """My request
        Provides login tool
        Basic Usage::
                >>> import weibo
                >>> ...

        """
        __attrs__ = ['arg', 'arg02']

        def __init__(self, arg=None):
                super(Myrequest, self).__init__()
                self.arg = arg
                self.arg02 = {}
                self.verify = True

        def __enter__(self):
                return self

        def __exit(self, *args):
                self.close()

        def myget(self):
                """Constructs a :class:`PreparedRequest <PreparedRequest>` for
        transmission and returns it. The :class:`PreparedRequest` has settings
        merged from the :class:`Request <Request>` instance and those of the
        :class:`Session`.

        :param request: :class:`Request` instance to prepare with this
            session's settings.
        """
                cookie = cookiejar.LWPCookieJar()
                cookie_support = request.HTTPCookieProcessor(cookie)
                opener = request.build_opener(cookie_support, request.HTTPHandler)
                request.install_opener(opener)
                url = 'http://www.baidu.com/'
                data = request.urlopen(url).read()
                print(data)

class Myrequests:
    def __init__(self):
        super(Myrequests, self).__init__()
    def myget(self):
        r = requests.get('https://github.com/timeline.json')
        pprint(r.text)
        print(r.status_code)
        print(r.headers['content-type'])


# Myrequest(1).myget()
# Myrequests().myget()


