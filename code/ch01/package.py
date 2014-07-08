
"""custom modules of yourself
"""
import hello,pprint
import drawing
import drawing.colors
from drawing import shapes



"""copy module examples
summary:
	__all__
	__doc__
	__file__ of functions&modules
"""
import copy
# from copy import * # only import functions in __all__ 
from copy import __all__

"""How to use [] in statement
"""
# pprint.pprint(__all__)
# pprint.pprint([n for n in dir(copy) if not n.startswith('_')])
# pprint.pprint(dir(copy))
# pprint.pprint(dir(sys))
# pprint.pprint(dir(drawing))
# pprint.pprint([n for n in dir(copy) if not n.startswith('_')])
# help(copy)
# help(copy.deepcopy)
# print(copy.copy.__doc__)
# print(sys.__doc__)
# help(sys)


# help(range)
# print(range.__doc__)
# print(copy.__file__)




"""sys module examples
"""
import sys
# sys.path.append('D:/Users/chengsiqin754/Downloads/github/Python/code/module')
# pprint.pprint(sys.path)

print(sys.platform)
# print(sys.argv)
# pprint.pprint(sys.modules)
# sys.exit("message")

args=sys.argv[1:]
# print(reversed(args[:]))
print(args.reverse())
print(' '.join(args))
# print(" ".join(reversed(args[:])))



"""os module examples
"""
import os
# os.system(r'D:\"python test way"\dairy.py')
# os.startfile(r'D:\python test way\dairy.py')
# os.system('echo %path%')



"""webbrowser module examples
"""
import webbrowser
webbrowser.open('www.baidu.com')



