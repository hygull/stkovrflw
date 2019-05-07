def traverse_dict(d, keys=[]):
	for key in d:
		keys.append(key)

		if type(d[key]) is dict:
			return keys + [traverse_dict(d[key], keys)]
		else:
			return keys

"""
{
	"a": {
		"b": 'v1',
		"c": 'v2'
	},
	"d": {
		"e": {
			"g": "v3"
			"h": "v4"
			"i": "v5"
		},
		"j": "v6"
	},
	"k": {
		"l": {
			"m": "v7",
			"n": "v8"
		},
		"o": {
			"p": "v9",
			"q": "v10",
			"r": {
				"s": {
					"t": 'v11',
					"u": "v12"
				},
				"v": "v13",
				"w": "v14",
				"x": {
					"y": {
						"z": "v15"
					}
				}
			}
		}
	}
}
"""