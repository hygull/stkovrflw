**@Selcuk**, you can try the below code examples.

> **Note:** You can't use statement like `{[1, 2, 3], [2, 3, 4], [2, 3, 4]}` in Python but `{[1, 2, 3], [2, 3, 4], [2, 3, 4]}`.
>
> So I will suggest you to use/create `[[1, 2, 3], [2, 3, 4], [2, 3, 4]]` type lists as a final result or you may use dictionay like `{'2018': {'10':['12-10-2018', '12-10-2018'], '11': ['12-11-2018', '9-11-2018']}}` to organize your dates based on year & month.


	>>> s = {[1, 2, 3], [2, 3, 4], [2, 3, 4]}
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: unhashable type: 'list'
	>>>
	>>> s = {(1, 2, 3), (2, 3, 4), (2, 3, 4)}
	>>> s
	set([(2, 3, 4), (1, 2, 3)])
	>>>

# &raquo; Example 1

	import json

	# List of dates
	list_dates = [
					'1-10-2018','4-10-2018','1-11-2018',
	            	'6-10-2018', '3-10-2018', '6-11-2018', 
	            	'9-11-2018'
	       		]

	d = {}

	for date in list_dates:
		day, month, year = date.split('-')

		if year in d:
			if month in d[year]:
				d[year][month].append(date)
			else:
				d[year][month] = [date]
		else:
			d[year] = {month: [date]}

	# Pretty printing d (Example 1.1: dictionary)
	print(json.dumps(d, indent=4))
	"""
		{
		    "2018": {
		        "11": [
		            "1-11-2018",
		            "6-11-2018",
		            "9-11-2018"
		        ],
		        "10": [
		            "1-10-2018",
		            "4-10-2018",
		            "6-10-2018",
		            "3-10-2018"
		        ]
		    }
		}
	"""

	# Creating and pretty printing list_grouped (Example 1.2: list of lists)
	list_grouped = [months_list for year in d.values() for months_list in year.values()]
	print(json.dumps(list_grouped, indent=4))
	"""
		[
		    [
		        "1-11-2018",
		        "6-11-2018",
		        "9-11-2018"
		    ],
		    [
		        "1-10-2018",
		        "4-10-2018",
		        "6-10-2018",
		        "3-10-2018"
		    ]
		]
	"""

# &raquo; Example 2

	# List of dates
	import json

	list_dates = [
					'1-10-2018','28-01-2017', '4-10-2018','1-11-2018',
	            	'6-10-2018', '3-10-2018', '6-12-2016', '6-11-2018', 
	            	'9-11-2018', '15-11-2016', '14-05-1992', '03-11-2017',
	            	'1-10-2018','25-01-2017', '4-11-2017','1-11-2016',
	            	'6-10-2018', '3-11-2016', '6-12-2017', '6-10-2013', 
	            	'9-12-2014', '15-10-2013', '20-05-1992', '03-12-2017',
	            	'19-12-2014', '15-10-2013', '20-05-1992', '03-12-2017'
	       		]

	d = {}

	for date in list_dates:
		day, month, year = date.split('-')

		if year in d:
			if month in d[year]:
				d[year][month].append(date)
			else:
				d[year][month] = [date]
		else:
			d[year] = {month: [date]}

	# Pretty printing d (Example 2.1: dictionary)
	print(json.dumps(d, indent=4))

	"""
		{
		    "1992": {
		        "05": [
		            "14-05-1992",
		            "20-05-1992",
		            "20-05-1992"
		        ]
		    },
		    "2018": {
		        "11": [
		            "1-11-2018",
		            "6-11-2018",
		            "9-11-2018"
		        ],
		        "10": [
		            "1-10-2018",
		            "4-10-2018",
		            "6-10-2018",
		            "3-10-2018",
		            "1-10-2018",
		            "6-10-2018"
		        ]
		    },
		    "2014": {
		        "12": [
		            "9-12-2014",
		            "19-12-2014"
		        ]
		    },
		    "2017": {
		        "11": [
		            "03-11-2017",
		            "4-11-2017"
		        ],
		        "12": [
		            "6-12-2017",
		            "03-12-2017",
		            "03-12-2017"
		        ],
		        "01": [
		            "28-01-2017",
		            "25-01-2017"
		        ]
		    },
		    "2016": {
		        "11": [
		            "15-11-2016",
		            "1-11-2016",
		            "3-11-2016"
		        ],
		        "12": [
		            "6-12-2016"
		        ]
		    },
		    "2013": {
		        "10": [
		            "6-10-2013",
		            "15-10-2013",
		            "15-10-2013"
		        ]
		    }
		}
	"""

	# Creating and pretty printing list_grouped (Example 2.2: list of lists)
	list_grouped = [months_list for year in d.values() for months_list in year.values()]
	print(json.dumps(list_grouped, indent=4))

	"""
		[
		    [
		        "14-05-1992",
		        "20-05-1992",
		        "20-05-1992"
		    ],
		    [
		        "1-11-2018",
		        "6-11-2018",
		        "9-11-2018"
		    ],
		    [
		        "1-10-2018",
		        "4-10-2018",
		        "6-10-2018",
		        "3-10-2018",
		        "1-10-2018",
		        "6-10-2018"
		    ],
		    [
		        "9-12-2014",
		        "19-12-2014"
		    ],
		    [
		        "03-11-2017",
		        "4-11-2017"
		    ],
		    [
		        "6-12-2017",
		        "03-12-2017",
		        "03-12-2017"
		    ],
		    [
		        "28-01-2017",
		        "25-01-2017"
		    ],
		    [
		        "15-11-2016",
		        "1-11-2016",
		        "3-11-2016"
		    ],
		    [
		        "6-12-2016"
		    ],
		    [
		        "6-10-2013",
		        "15-10-2013",
		        "15-10-2013"
		    ]
		]
	"""

