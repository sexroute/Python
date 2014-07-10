
def dive(x,y):
	try:
		result = x/y
	except ZeroDivisionError as z:
		print('wrong.', z)
	else:
		print('the result is ', result)
	finally:
		print('executing finally caluse.')

def raise_test():
	try:
		result = 1/0
	except ZeroDivisionError:
		print("can't process the exception")
		raise
	finally:
		print("in finally ")



if __name__ == '__main__':
	# dive()
	raise_test()
