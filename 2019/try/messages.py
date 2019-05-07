import json

profile = {
	"Person":{
		"name":{
			"First_Name":["John"], 
			"Last_Name":['Doe']
		}
	}, 
	"Object":{
		"name":{
			"First_Name":['John'], 
			"Last_Name":['Doe']
		}
	}
}

# START
messages = []
for key1 in profile:
	for key2 in profile[key1]:
		for key3 in profile[key1][key2]:
			message = "{0} is a {1} and is located in profile['{2}']['{3}']['{4}']"
			messages.append(message.format(key3, 'key', key1, key2, key3))
			messages.append(message.format(profile[key1][key2][key3][0], 'value', key1, key2, key3))

# --- Pretty print the list `messages` (indentation 4) ---
print(json.dumps(messages, indent=4))
# [
#     "First_Name is a key and is located in profile['Person']['name']['First_Name']",
#     "John is a value and is located in profile['Person']['name']['First_Name']",
#     "Last_Name is a key and is located in profile['Person']['name']['Last_Name']",
#     "Doe is a value and is located in profile['Person']['name']['Last_Name']",
#     "First_Name is a key and is located in profile['Object']['name']['First_Name']",
#     "John is a value and is located in profile['Object']['name']['First_Name']",
#     "Last_Name is a key and is located in profile['Object']['name']['Last_Name']",
#     "Doe is a value and is located in profile['Object']['name']['Last_Name']"
# ]


# --- As a string ---
print('\n'.join(messages))
# First_Name is a key and is located in profile['Person']['name']['First_Name']
# John is a value and is located in profile['Person']['name']['First_Name']
# Last_Name is a key and is located in profile['Person']['name']['Last_Name']
# Doe is a value and is located in profile['Person']['name']['Last_Name']
# First_Name is a key and is located in profile['Object']['name']['First_Name']
# John is a value and is located in profile['Object']['name']['First_Name']
# Last_Name is a key and is located in profile['Object']['name']['Last_Name']
# Doe is a value and is located in profile['Object']['name']['Last_Name']