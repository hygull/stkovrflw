def func3(a):
	a/0;

def func2(a, b):
	func3(a);

def func1(a, b, c):
	func2(a, b);

if __name__ == "__main__":
	func1(12, 0, 89)