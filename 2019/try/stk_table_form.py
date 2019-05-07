import json

# `null` is used in JavaScript (JSON is JavaScript), so I considered it as string
json_text = """[{"itemcode":null,"productname":"PKS543452","value_2018":null},
{"itemcode":null,"productname":"JHBG6%&9","value_2018":null},
{"itemcode":null,"productname":"VATER3456","value_2018":null},
{"itemcode":null,"productname":"ACDFER3434","value_2018":null}]"""

# Will contain the rows (text)
texts = []

# Converting to original list object, `null`(JavaScript) will transform to `None`(Python)
l = json.loads(json_text)

# Obtain keys (Note that dictionary is an unorederd data type)
# So it is imp to get keys for ordered iteration in all dictionaries of list
# Column may be in different position but related data will be perfect
# If you wish you can hard code the `keys`, here I am getting using `l[0].keys()`
keys = l[0].keys()

# Form header and add to `texts` list
header = '|' + ' | '.join(keys) + " |"
texts.append(header)

# Form body (rows) and append to `texts` list
rows = ['| ' + "|".join(["null" if d[key] is None else d[key] for key in keys]) + "|" for d in l]
texts.extend(rows)

# Print all rows (including header) separated by newline '\n'
answer = '\n'.join(texts)
print(answer)

