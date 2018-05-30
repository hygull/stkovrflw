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