import fileinput

for line in fileinput.input(inplace=False):
	line = line.rstrip()
	num = fileinput.lineno()
	print('%-40s # %2i' % (line, num))


# print(set(range(10)))
a=set([1,2,3])
b=set([2,5,4])
c=a&b
print(a.union(b))
print(a|b)
print(c.issubset(a))
print(c<=a)
# help(a.intersection)
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
# help(a.symmetric_difference)


import re
help(re.sub)
