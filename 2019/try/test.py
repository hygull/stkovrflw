def f1():
	print("F1")
	return 1

def f2():
	print("F2")
	return 22

def f3():
	print("F3")
	return 333


def f3():
	print("F4")
	return 4444


class User(object):
	a = f1()
	b = f2()

	def __init__(self):
		self.d = f3()

	def cat(self):
		self.c = f4()



print(User.a)
print(User.b)
print(User.a)
