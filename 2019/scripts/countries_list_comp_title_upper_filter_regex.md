https://stackoverflow.com/questions/57132687/how-to-print-name-from-a-list-dict-where-the-first-element-is-t-and-second-is-a

```python
>>> import re
>>> 
>>> countries = ["Bangladesh", "taiwan", "Srilanka", "India", "tAjikistan", "Tanzania", "Pakistan"]
>>> 
>>> new_countries = [country for country in countries if re.match(r"^[tT][aA]", country)]
>>> new_countries
['taiwan', 'tAjikistan', 'Tanzania']
>>> 
>>> # If you want matched country names in caps 
... 
>>> new_countries = [country.upper() for country in countries if re.match(r"^[tT][aA]", country)]
>>> new_countries
['TAIWAN', 'TAJIKISTAN', 'TANZANIA']
>>> 
>>> # If you want matched country names in title case
... 
>>> new_countries = [country.title() for country in countries if re.match(r"^[tT][aA]", country)]
>>> new_countries
['Taiwan', 'Tajikistan', 'Tanzania']
>>> 
>>> 
```

