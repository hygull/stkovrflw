
class B(object):
	def ok2(self):
		print("Great")

class A(object):
	def ok(self):
		b = B()
		b.ok2()

a = A()
a.ok()


