
def f1(self, x, y):
	return min(x, x+y)

class C:
	"""docstring for C"""
	arg = 'class_arg'
	def __init__(self, arg='__init__arg'):
		super(C, self).__init__()
		self.arg = arg
	def g(self):
		return 'hello'
	h = g


def scope_test():
	def do_local():
		spam = 'local_spam'
	def do_nonlocal():
		nonlocal spam
		spam = 'nonlocal spam'
	def do_global():
		global spam
		spam = 'global spam'
	spam = 'test spam'
	do_local()
	print("After local assignment:", spam)
	do_nonlocal()
	print("After nonlocal assignment:", spam)
	do_global()
	print("After global assignment:", spam)
# scope_test()
# print("In global scope:", spam)


class Bag:
	"""docstring for Bag"""
	def __init__(self):
		super(Bag, self).__init__()
		self.data = []
	def add(self, x):
		self.data.append(x)
	def addtwice(self, x):
		self.add(x)
		self.add(x)
# b = Bag()
# b.addtwice('add')
# print(b.data)


var = 'global_var'
class Global_test:
	"""docstring for Global_test"""
	def __init__(self):
		super(Global_test, self).__init__()
		global var
		print(var)
# var = 'global_var2'
# Global_test()


# ?python super()
def mydir():
	import sys
	from pprint import pprint
	pprint(dir(object))


def myisubclass():
	print(isinstance(tuple, object))
	print(issubclass(tuple, object))


def mylambda():
	pass
	return lambda x:x**3
def mylambda02():
	mydict = {'a':1,'b':2,'c':3}
	print(mydict)
def myfor():
	mydict = {'a':1,'b':2,'c':3}
	print([x for x in mydict if mydict[x] % 2 == 0])
	print((lambda :1)())
# print(mylambda()(4))
# mylambda02()
# myfor()



