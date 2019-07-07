**@Naji**, have a look at below code:

> You can use **int()** and **bin()** functions multiple times to satify your goal.

	a = 10000
	b = 1

	# Base 2 addition
	result1 = (bin( int(str(a), 2) - int(str(b), 2) )[2:] # 1111

	# Base 2 subtraction
	result2 = bin( int(str(a), 2) + int(str(b), 2) )[2:]  # 10001

### &raquo; A try on Python's interactive console

	>>> # Base 2 subtraction & addition 
	...
	>>> a = 10000
	>>> b = 1
	>>>
	>>> result = bin( int(str(a), 2) - int(str(b), 2) )
	>>> result
	'0b1111'
	>>>
	>>> result = bin( int(str(a), 2) + int(str(b), 2) )
	>>> result
	'0b10001'
	>>>
	>>> result = bin( int(str(a), 2) - int(str(b), 2) )[2:]
	>>> result
	'1111'
	>>>
	>>> result = bin( int(str(a), 2) + int(str(b), 2) )[2:]
	>>> result
	'10001'
	>>>

Let's try to add all the binary numbers that you have specified in the problem.

	>>> binaries = [10000, 10001, 10010, 10011, 10100, 10101, 10110, 10111, 11000, 11001, 11010, 11011, 11100, 11101, 11110, 11111]
	>>>
	>>> decimals = [int(str(binary), 2) for binary in binaries]
	>>> decimals
	[16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
	>>>
	>>> sum(decimals)
	376
	>>>
	>>> bin(sum(decimals))
	'0b101111000'
	>>>
	>>> bin(sum(decimals))[2:]
	'101111000'
	>>>

Finally, we can design our own method that will result exact binay string (i.e. without `0b` prepended as in `0b1111`) after addition or subtraction.


	# ********* BASE2 ADDITION ***************
	def base2_addition(a, b):
		try:
			int_a = int(str(a), 2) 
			int_b = int(str(b), 2) 

			return bin(int_a + int_b)[2:] 
		except:
			print ("Invalid input provided (Expected 2 binary strings/numbers with 0s and 1s")
			return None

	print base2_addition('10000', '1')   # 10001
	print base2_addition('10001', '011') # 10100

	# ********* BASE SUBTRACTION **************
	def base2_subtraction(a, b):
		try:
			int_a = int(str(a), 2) 
			int_b = int(str(b), 2) 

			return bin(int_a - int_b)[2:] 
		except:
			print ("Invalid input provided (Expected 2 binary strings/numbers with 0s and 1s")
			return None

	print(base2_subtraction('10100', '101')) # 1111