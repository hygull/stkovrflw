# -*- coding: utf-8 -*-
import requests
import json
url="https://www.umass.edu/peoplefinder/"

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
searchData={'q': 'Alex'}
response=requests.post(url, data=json.dumps(searchData), headers=headers)
# content = response.json()  
# print(content)
print(response.__dict__)

for k in response.__dict__:
	print(k)
# print(response.text.encode('utf-8'))