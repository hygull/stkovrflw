## Where is the problem in your code?

> In Python, dictionary is defined as an unordered collection of key-value paired items where keys are unique and immutable objects.

The `update()` method updates the calling dictionary object i.e. **`x`** with the contents of passing dictinary object i.e. **`y`**.

If it finds any duplicated key in the calling object then it will override its value with the value corresponding to the matched key of passing object.

	x = {'a':1, 'b': 2}
	y = {'b':10, 'c': 11}

> So you will get `{'a': 1, 'b': 10, 'c': 11}` in place of getting `{'a': 1, 'b': 10, 'c': 11, 'b': 2}`


## Use dictionary comprehension to solve

The professional way to create dictionaries using existing dictionaries or other iterator objects.

	>>> x = {'a':1, 'b': 2}
	>>> y = {'b':10, 'c': 11}
	>>>
	>>> my_dicts = (x, y); 	# Gathering all dictionaries in a tuple/list
	>>> z = {key: value for my_dict in my_dicts for key, value in my_dict.iteritems()}; # Single line of code that creates new dictionary object from existing dictionaries
	>>> z
	{'a': 1, 'c': 11, 'b': 10}

## References

https://www.datacamp.com/community/tutorials/python-dictionary-comprehension

Thanks.

