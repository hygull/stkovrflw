def find_in_input_json(element, input_json):
	values = {} # Output dictionary with key in dict1: matched value

	for d_f in dict1:
		path = dict1[d_f] 		# "s0/s1/s1_f1"
		paths = path.split('/') # ['s0', 's1', 's1_f1']
		rv = input_json

		for s in paths: # s: s0 -> s1 -> s1_f1 (one by one)
			if s in rv:
				rv = rv[s] # Update input_json with new dictionary pointed by current matched key

		values[d_f] = rv # {'d0_f1': 's1_v1'} ->  {'d0_f1': 's1_v1', 'd3_f1': 's3_v1'} -> so...on

	return values


if __name__ == '__main__':
	dict1 = {
	    "d0_f1": "s0/s1/s1_f1",
	    "d3_f1": "s0/s2/s2_f3/s3_f1",
	    "d1_f1": "s0/s2/s2_f1",
	    "d1_f2": "s0/s2/s2_f2"
	}

	dict2 = {
	    "s0": {
	        "s1": {
	            "s1_f1": "s1_v1",
	            "s1_f2": "s1_v2"
	        },
	        "s2": {
	            "s2_f1": "s2_v1",
	            "s2_f2": "s2_v2",
	            "s2_f3": {
	                "s3_f1": "s3_v1"
	            }
	        }
	    }
	}

	values = find_in_input_json(dict1, dict2)
	print(values) # {'d0_f1': 's1_v1', 'd3_f1': 's3_v1', 'd1_f1': 's2_v1', 'd1_f2': 's2_v2'}