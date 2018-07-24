> https://stackoverflow.com/questions/51483197/pasting-data-from-multiple-dictionary-into-a-csv-with-python/51485306#51485306
Just 2 lines are enough.

	new_strmyDict1 = re.sub('\[\s+', '[', strmyDict)
	new_strmyDict2 = re.sub('\}\s+', '}',new_strmyDict1)

Below is the explanation of above 2 statements.

### Input string &raquo;

	>>> strmyDict = '{\n "setA": [\n  {\n   "name": "kranthi"\n  },\n  {\n   "place": "kranth
	i"\n  }\n ],\n "setB": [\n  {\n   "number": 1\n  }\n ],\n "setC": "My string"\n}'
	>>>
	>>> strmyDict
	'{\n "setA": [\n  {\n   "name": "kranthi"\n  },\n  {\n   "place": "kranthi"\n  }\n ],\n "
	setB": [\n  {\n   "number": 1\n  }\n ],\n "setC": "My string"\n}'
	>>>
	>>> print strmyDict
	{
	 "setA": [
	  {
	   "name": "kranthi"
	  },
	  {
	   "place": "kranthi"
	  }
	 ],
	 "setB": [
	  {
	   "number": 1
	  }
	 ],
	 "setC": "My string"
	}
	>>>


### Output &raquo;

	>>> new_strmyDict1 = re.sub('\[\s+', '[', strmyDict)
	>>> new_strmyDict1
	'{\n "setA": [{\n   "name": "kranthi"\n  },\n  {\n   "place": "kranthi"\n  }\n ],\n "setB
	": [{\n   "number": 1\n  }\n ],\n "setC": "My string"\n}'
	>>>
	>>> print new_strmyDict1
	{
	 "setA": [{
	   "name": "kranthi"
	  },
	  {
	   "place": "kranthi"
	  }
	 ],
	 "setB": [{
	   "number": 1
	  }
	 ],
	 "setC": "My string"
	}
	>>>
	>>> new_strmyDict2 = re.sub('\}\s+', '}',new_strmyDict1)
	>>> new_strmyDict2
	'{\n "setA": [{\n   "name": "kranthi"\n  },\n  {\n   "place": "kranthi"\n  }],\n "setB":
	[{\n   "number": 1\n  }],\n "setC": "My string"\n}'
	>>>
	>>> print new_strmyDict2
	{
	 "setA": [{
	   "name": "kranthi"
	  },
	  {
	   "place": "kranthi"
	  }],
	 "setB": [{
	   "number": 1
	  }],
	 "setC": "My string"
	}
	>>>


