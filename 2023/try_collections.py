from collections import Counter

d = ['a', 'b', '2', 2, '11', '1', '1', 11, '89', '89', '89', '90']
counts = Counter(d)
print(counts) # Counter({'89': 3, '1': 2, 'a': 1, 'b': 1, '2': 1, 2: 1, '11': 1, 11: 1, '90': 1})

# Loop through items
for key, value in counts.items():
	print(key, '->', value)
	'''
	a -> 1
	b -> 1
	2 -> 1
	2 -> 1
	11 -> 1
	1 -> 2
	11 -> 1
	89 -> 3
	90 -> 1
	'''

# New Dictionary (Updating the dictionary by using the elements from another dict like object created using collections) 
numbers = {
	'one': 1,
	'two': 2
}
numbers.update(counts)
print(numbers) # {'one': 1, 'two': 2, 'a': 1, 'b': 1, '2': 1, 2: 1, '11': 1, '1': 2, 11: 1, '89': 3, '90': 1}

# using fromkeys() to create dict with keys and default values
d1 = dict.fromkeys(['a', 'b', 'c']) # {'a': None, 'b': None, 'c': None}
d2 = dict.fromkeys(['a', 'b', 'c'], 0) # {'a': 0, 'b': 0, 'c': 0}