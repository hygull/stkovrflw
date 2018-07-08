# Q

slice certain parts of a string inside an array into another array, for example consider their is an array data

data = ["xbox 360 | 13000 | new","playstation 4 | 30000 | new","playstation 3 | 30000 | old","playstation 2 | 30000 | old"]

i want to slice each component into three,
**@surya**, you can also use **list comprehension** with **reduce()** method to accomplish your task just with the use of 1 line statement  `products, cost, condition = reduce(lambda s1, s2: [s1[index] + [item.strip()] for index, item in enumerate(s2.split('|'))], data,[[], [], []])`. 
product = ["xbox 360","playstation 4","playstation 3","playstation 2"]

cost = ["13000","30000","30000","30000"]



condition = ["new","new","old","old"]

# Q link
https://stackoverflow.com/questions/51229187/how-to-slice-strings-inside-array-into-another-array-using-python/51229312#51229312

# A

**@surya**, you can try any one of the below 2 approaches. The 1st one is very short which will give your all 3 lists just with an execution of one line statement. I have used he concept of **list comprehension** and **reduce()** function.

> Use **split()** to get the words separated with `|` for each of the list items.
>
> Use **strip()** to remove leading/trailing whitespaces. 

## 1st way (one line statement)

> Just use `product, cost, condition = reduce(lambda s1, s2: [s1[index] + [item.strip()] for index, item in enumerate(s2.split('|'))], data,[[], [], []]);` and it will give your lists.

	>>> data = ["xbox 360 | 13000 | new","playstation 4 | 30000 | new","playstation 3 | 30000 | old","playstation 2 | 30000 | old"]
	>>>
	>>> product, cost, condition = reduce(lambda s1, s2: [s1[index] + [item.strip()] for index, item in enumerate(s2.split('|'))], data,[[], [], []]);
	>>>
	>>> product
	['xbox 360', 'playstation 4', 'playstation 3', 'playstation 2']
	>>>
	>>> cost
	['13000', '30000', '30000', '30000']
	>>>
	>>> condition
	['new', 'new', 'old', 'old']
	>>>

## 2nd way

	>>> data = ["xbox 360 | 13000 | new","playstation 4 | 30000 | new","playstation 3 | 30000 | old","playstation 2 | 30000 | old"]
	>>>
	>>> product = []
	>>> cost = []
	>>> condition = []
	>>>
	>>> for s in data:
	...     l = [item.strip() for item in s.split("|")]
	...     product.append(l[0])
	...     cost.append(l[1])
	...     condition.append(l[2])
	...
	>>> product
	['xbox 360', 'playstation 4', 'playstation 3', 'playstation 2']
	>>>
	>>> cost
	['13000', '30000', '30000', '30000']
	>>>
	>>> condition
	['new', 'new', 'old', 'old']
	>>>
	>>>
















































