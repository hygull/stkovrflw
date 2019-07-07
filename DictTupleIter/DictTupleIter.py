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

