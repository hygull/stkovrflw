You may also try the below code.

def get_count(t, year):
	count = 0

	for item in t:
		if type(item) is str:
			if year in item:
				count += 1
		elif type(item) is tuple:
				if int(year) in item or year in item:
					count += 1
		elif type(item) is int:
			if int(year) == item:
				count += 1
			
	return count

# START
if __name__ == "__main__":
	# INPUT 1
	year = input("Enter a year")

	t = (("Steve"), ("Carell"), (16, "August", 1962),
	            "Actor", ("Concord", "Massachusetts"))

	count = get_count(t, year)
	print(count)

	# INPUT 2
	year = input("Enter a year")

	t = (("Steve"), ("Carell", 1962), (16, "August", 1962),
	            "Actor", ("Concord", "Massachusetts"))

	count = get_count(t, year)
	print(count) # 2

	# INPUT 3
	year = input("Enter a year")

	t = (("1962"), ("Carell", 1962), (16, "August", 1962),
	            "Actor", ("Concord", "Massachusetts"), 1962)

	count = get_count(t, year)
	print(count) # 4

