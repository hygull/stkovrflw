import json

with open('Data.json', 'r') as f:
	data = f.read().strip();

# String
print(data)
print(type(data))
"""
{"Key":"MyValue","KeyTwo":{"KeyThree":"Value Two"}}
<type 'str'>
"""

# 1st way
dict1 = eval(data) # KeyError, if your JSON data is not in correct form
print(dict1)
print(type(dict1))
"""
	{'KeyTwo': {'KeyThree': 'Value Two'}, 'Key': 'MyValue'}
	<type 'dict'>
"""

# 2nd way
dict2 = json.loads(data) # ValueError, if your JSON data is not in correct form
print(dict2)
print(type(dict2))
"""
	{u'KeyTwo': {u'KeyThree': u'Value Two'}, u'Key': u'MyValue'}
	<type 'dict'>
"""

