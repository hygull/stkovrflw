**@Tjaart**, based on your inputs and expected outputs, the following code will work as expected. 

> Please try it and let me know if it fails for any of your input.

	"""
	INPUTS AND EXPECTED OUTPUTS:-

		9     => "1001"
		60    => "0011_1100"
		100   => "0110_0100"
		63000 => "1111_0110_0001_1000"
	"""
	def get_binary(n):
		s = bin(n)[2:]; # Getting binary string

		strs = [];

		while s:
			l = len(s);     # Finding lenght of binary string

			if l > 4:
				strs.insert(0, s[l-4:]);
				s = s[:l-4];
			else:
				l = len(s);
				s = "0"*(4-l) + s;  # If length is not equal to 4 (modify it by adding 0s to front)
				strs.insert(0, s);
				s = "";
		
		return "_".join(strs);

	# EXAMPLE 1
	a = 9;
	print(get_binary(a)); # 1001

	# EXAMPLE 2
	b = 60;
	print(get_binary(b)); # 0011_1100

	# EXAMPLE 3
	c = 100;
	print(get_binary(c)); # 0110_0100

	# EXAMPLE 4
	d = 63000;
	print(get_binary(d)); # 1111_0110_0001_1000