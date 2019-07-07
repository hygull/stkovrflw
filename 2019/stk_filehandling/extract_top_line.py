# https://stackoverflow.com/questions/55410134/python-code-to-extract-the-data-from-out-file/55410727#55410727
# Solved: 29 March 2019, Fri

with open("data.txt") as f:
	lines = f.readlines()

	# As your line is in 2nd place, it will be lines[1] {0 based index}
	line = lines[1].strip() # strip() is to remove any '\n' from start/end of line
	
	print(line)
	# 000003c80e06 - 000-00634-42438-177 - Thu Mar 28 13:17:42 GMT 2019

	arr = line.split(" - ")
	print(arr)
	# ['000003c80e06', '000-00634-42438-177', 'Thu Mar 28 13:17:42 GMT 2019']

	# --*-- If you want to store it in a dictionary then you can do like this --*--
	d = {
		"mac_address": arr[0],
		"unit_address": arr[1],
		"execution_time": arr[2]
	}
	print(d)
	# {'execution_time': 'Thu Mar 28 13:17:42 GMT 2019', 'unit_address': '000-00634-42438-177', 'mac_address': '000003c80e06'}

	# --*-- If you want to pretty print the above dict --*--
	import json
	pretty_d = json.dumps(d, indent=4)
	print(pretty_d)
	# {
	#     "execution_time": "Thu Mar 28 13:17:42 GMT 2019", 
	#     "unit_address": "000-00634-42438-177", 
	#     "mac_address": "000003c80e06"
	# }


# Markdown on Sof

"""
You can try like this.

I have stored the desired o/p in 2 formats. As an array `['000003c80e06', '000-00634-42438-177', 'Thu Mar 28 13:17:42 GMT 2019']` and as a dictionary `{'execution_time': 'Thu Mar 28 13:17:42 GMT 2019', 'unit_address': '000-00634-42438-177', 'mac_address': '000003c80e06'}`.

> Read comments to know about what actually the related statements are doing.

	with open("data.txt") as f:
		lines = f.readlines()

		# As your line is in 2nd place, it will be lines[1] {0 based index}
		line = lines[1].strip() # strip() is to remove any '\n' from start/end of line
		
		print(line)
		# 000003c80e06 - 000-00634-42438-177 - Thu Mar 28 13:17:42 GMT 2019

		arr = line.split(" - ")
		print(arr)
		# ['000003c80e06', '000-00634-42438-177', 'Thu Mar 28 13:17:42 GMT 2019']

		# --*-- If you want to store it in a dictionary then you can do like this --*--
		d = {
			"mac_address": arr[0],
			"unit_address": arr[1],
			"execution_time": arr[2]
		}
		print(d)
		# {'execution_time': 'Thu Mar 28 13:17:42 GMT 2019', 'unit_address': '000-00634-42438-177', 'mac_address': '000003c80e06'}

		# --*-- If you want to pretty print the above dict --*--
		import json
		pretty_d = json.dumps(d, indent=4)
		print(pretty_d)
		# {
		#     "execution_time": "Thu Mar 28 13:17:42 GMT 2019", 
		#     "unit_address": "000-00634-42438-177", 
		#     "mac_address": "000003c80e06"
		# }
"""