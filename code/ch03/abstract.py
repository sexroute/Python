
def fibonacci():
	fibs = [0, 1]
	for x in xrange(8):
		fibs.append(fibs[-2] + fibs[-1])
	return fibs
# print fibonacci()


from random import choice
x = choice(['Hello, world!', [1, 2, 'e', 'e', 4]])
# print x.count()

class Object():
	"""docstring for object"""
	def __init__(self, arg):
		self.arg = arg

class Class:
	"""docstring for Class"""
	def method(self):
		print 'method!'
	_var = 'Hello'
# print Class._var
def function():
	print 'function!'
instance = Class()
# instance.method()
# instance.method = function
# instance.method()
# fun = instance.method
# fun()

# obj = Object(1)
# obj.you = function
# obj.you()




class C:
	"""docstring for C"""
	# print 'Class C being defined...'
	pass
# C()


class MemeberCounter:
	"""docstring for MemeberCounter"""
	members = 0
	def init(self):
		MemeberCounter.members += 1
# m1 = MemeberCounter()
# print MemeberCounter.members
# m1.init()
# print MemeberCounter.members
# m1.members = "m1.members"
# print m1.members
# print MemeberCounter.members
# m1.number = "m1.number"
# print m1.number
# MemeberCounter.number = "MemeberCounter.number"
# print MemeberCounter.number
# MemeberCounter.google = "MemeberCounter.google"
# print MemeberCounter.google


class Filter:
	"""docstring for Filter"""
	def init(self):
		self.blocked = []
	def filter(self, sequence):
		return [x for x in sequence if x not in self.blocked]
class SPAMFilter(Filter):
	"""docstring for SPAMFilter"""
	def init(self):
		self.blocked = ['SPAM']
# f = Filter()
# f.init()
# print f.filter((1,2,3,4))
# s = SPAMFilter()
# print isinstance(s, SPAMFilter)
# print isinstance(s, Filter)
# s.init()
# print s.filter(["SPAM", "SPAM", 'SPAM', "SPMA2"])

# print issubclass(SPAMFilter, Filter)
# print issubclass(Filter, SPAMFilter)
# print SPAMFilter.__bases__
# print Filter.__bases__
# print isinstance(SPAMFilter(), object)
# print issubclass(SPAMFilter, object)
# print SPAMFilter().__class__


class Calculator:
	"""docstring for Calculator"""
	def caclulator(self, expression):
		self.value = eval(expression)
class Talker:
	"""docstring for Talker"""
	def talk(self):
		print 'value is', self.value
class TalkingCalculator(Calculator, Talker):
	"""docstring for TalkingCalculator"""
	pass
tc = TalkingCalculator()
# tc.caclulator('2*6')
# tc.talk()
# print hasattr(TalkingCalculator(), 'talk')
# print hasattr(TalkingCalculator(), 'fnord')
# print eval("1+2")
# print callable(getattr(TalkingCalculator(), 'caclulator'))
# print callable(getattr(TalkingCalculator(), 'talk'))
# setattr(tc, 'who', 'MR.')
# print tc.who
# print tc.__dict__



def bind(self):
	pass
# bind.value = 'bing.value'
# print bind.value


# print map(str, range(10))
def func(x):
	return x.isalnum()
seq = ["foo", "x41", "?!", "***"]
# print filter(func, seq)
# print [x for x in seq if x.isalnum()]
# print filter(lambda x : x.isalnum(), seq)
# print reduce(lambda x,y: x+y, range(10))

class A(object):
	"""docstring for A"""
	def __init__(self):
		super(A, self).__init__()
		print 'A init'
		self.__valueA = "__valueA"
		self._valueA = "_valueA"
class B(object):
	"""docstring for B"""
	def __init__(self):
		super(B, self).__init__()
		print 'B init'
	def valueB(self):
		print A()._valueA
class C(A,B):
	"""docstring for C"""
	def __init__(self):
		super(C, self).__init__()
		# A.__init__(self)
		# B.__init__(self)
	def valueC(self):
		print self._A__valueA
		print self._valueA
# C()
		
C().valueC()
# B().valueB()



