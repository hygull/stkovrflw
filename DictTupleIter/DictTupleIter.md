You can also try the below code. The code is based on the concept of `list comprehension`, & `deepcopy() operation` in Python. 

> Check [Shallow copy vs deepcopy in Python](https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/).

	import pprint;
	import copy;

	data = {
		'a': 0,
		'b': 1,
		'c': [0, 1, 2],
		'pair': ['one','two'],
	};

	def get_updated_dict(data, index, pair_name):
		d = copy.deepcopy(data);
		d.update({'c': index, 'pair': pair_name});
		return d;

	output = [tuple(get_updated_dict(data, index, pair_name) for pair_name in data['pair']) for index in data['c']];

	# Pretty printing the output list.
	pprint.pprint(output, indent=4);

Output &raquo;

	[   (   {   'a': 0, 'b': 1, 'c': 0, 'pair': 'one'},
	        {   'a': 0, 'b': 1, 'c': 0, 'pair': 'two'}),
	    (   {   'a': 0, 'b': 1, 'c': 1, 'pair': 'one'},
	        {   'a': 0, 'b': 1, 'c': 1, 'pair': 'two'}),
	    (   {   'a': 0, 'b': 1, 'c': 2, 'pair': 'one'},
	        {   'a': 0, 'b': 1, 'c': 2, 'pair': 'two'})]



Pretty printing using json module &raquo;

> **Note:** Tuple will convert into list here as tuples are not supported inside JSON.

	import json;
	print(json.dumps(output, indent=4));
	
	[
	    [
	        {
	            "a": 0,
	            "c": 0,
	            "b": 1,
	            "pair": "one"
	        },
	        {
	            "a": 0,
	            "c": 0,
	            "b": 1,
	            "pair": "two"
	        }
	    ],
	    [
	        {
	            "a": 0,
	            "c": 1,
	            "b": 1,
	            "pair": "one"
	        },
	        {
	            "a": 0,
	            "c": 1,
	            "b": 1,
	            "pair": "two"
	        }
	    ],
	    [
	        {
	            "a": 0,
	            "c": 2,
	            "b": 1,
	            "pair": "one"
	        },
	        {
	            "a": 0,
	            "c": 2,
	            "b": 1,
	            "pair": "two"
	        }
	    ]
	]

