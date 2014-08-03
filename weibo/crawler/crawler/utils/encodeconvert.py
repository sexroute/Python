# -*- coding: utf-8 -*-

def uprint(obj):
	import re
	print re.sub(r"\\u([a-f0-9]{4})",lambda mg: unichr(int(mg.group(1),16)),obj.__repr__())

def uprint02(obj):
	str_obj = str(obj).replace('u\'','\'').decode('unicode-escape')
	print str_obj

def byteprint(obj):
	print json.dumps(obj,encoding='utf-8',ensure_ascii=False)

