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



# -----------
'''
In [1]: l = range(10)

In [2]: l
Out[2]: range(0, 10)

In [3]: for n in l:
   ...:     print(n)
   ...: 
0
1
2
3
4
5
6
7
8
9

In [4]: d = dict.fromkeys(range(10))

In [5]: print(d)
{0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}

In [6]: 
'''

# -----------

'''
In [11]: d = dict.fromkeys(range(10))

In [12]: for k in d:
    ...:     d[k] = bool(d[k]) + 2
    ...:     print(d)
    ...: 
{0: 2, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}
{0: 2, 1: 2, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}
{0: 2, 1: 2, 2: 2, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}
{0: 2, 1: 2, 2: 2, 3: 2, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}
{0: 2, 1: 2, 2: 2, 3: 2, 4: 2, 5: None, 6: None, 7: None, 8: None, 9: None}
{0: 2, 1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: None, 7: None, 8: None, 9: None}
{0: 2, 1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: None, 8: None, 9: None}
{0: 2, 1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: None, 9: None}
{0: 2, 1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: None}
{0: 2, 1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2}
''''