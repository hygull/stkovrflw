import sys, traceback

def func3(a):
	a/0;

def func2(a, b):
	func3(a);

def func1(a, b, c):
	func2(a, b);

if __name__ == "__main__":
	try:
		func1(12, 0, 89)
	except:
		exc_type, exc_value, exc_traceback = sys.exc_info()
		
		# exc_type below is ignored on 3.5 and later
		exception_messages = traceback.format_exception(exc_type, exc_value,
                                          exc_traceback)

		for exception_message in exception_messages:
			print("-----------------------------------------------------------------------")
			print(exception_message)
		


