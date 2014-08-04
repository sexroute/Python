# -*- coding: utf-8 -*-

# 查看更多微博»
# <a bpfilter=\\\"page\\\" class=\\\"PRF_feed_list_more SW_fun_bg S_line2\\\" href=\\\"(.*?)\\\"><span>查看更多微博»<\\\/span><\\\/a>
# <a bpfilter=\\\\\"page\\\\\" class=\\\\\"PRF_feed_list_more SW_fun_bg S_line2\\\\\" href=\\\\\"(.*?)\\\\\"><span>查看更多微博»<\\\\\/span><\\\\\/a>

import re
with open(r'd:\allovince.html','r') as f:
	text = f.read()
	# print text
	print re.search("<a bpfilter=\\\\\"page\\\\\" class=\\\\\"PRF_feed_list_more SW_fun_bg S_line2\\\\\" href=\\\\\"(.*?)\\\\\"><span>查看更多微博»<\\\\\/span><\\\\\/a>",text).group(1)
	# next = re.search("href=\"(.*?)\"><span>查看更多微博»<\/span>",text).group(1)
	# print next
