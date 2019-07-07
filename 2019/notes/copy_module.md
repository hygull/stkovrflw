```bash
>>> import copy
>>> 
>>> details = {
...     "age": 1,
...     "langs": ["Python", "C", "Java", "JavaScript", "C++", "Golang"],
...     "brother": {
...         "age": 2,
...         "fullname": "Hemkesh Agrawani"
...     },
...     "fullname": "Rishikesh Agrawani"
... }
>>> 
>>> data = details
>>> 
>>> id(data)
4454135992
>>> 
>>> id(details)
4454135992
>>> 
>>> for k in details:
...     print(k, id(k), " : ", details[k], id(details[k]))
... 
age 4456268496  :  1 4451772352
langs 4456268160  :  ['Python', 'C', 'Java', 'JavaScript', 'C++', 'Golang'] 4456230792
brother 4456268720  :  {'age': 2, 'fullname': 'Hemkesh Agrawani'} 4454135920
fullname 4453255856  :  Rishikesh Agrawani 4456296496
>>> 
>>> for k in data:
...     print(k, id(k), " : ", data[k], id(data[k]))
... 
age 4456268496  :  1 4451772352
langs 4456268160  :  ['Python', 'C', 'Java', 'JavaScript', 'C++', 'Golang'] 4456230792
brother 4456268720  :  {'age': 2, 'fullname': 'Hemkesh Agrawani'} 4454135920
fullname 4453255856  :  Rishikesh Agrawani 4456296496
>>> 
```


