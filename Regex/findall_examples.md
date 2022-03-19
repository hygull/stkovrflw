# findall() example

```python
In [9]: import re                                                                                             

In [10]: sentence = "This year is the 1 among past 2 years with similar experice I had in 3rd of march"       

In [11]: re.findall(r'\d+', sentence)                                                                         
Out[11]: ['1', '2', '3']

In [12]: sum([int(s) for s in re.findall(r'\d+', sentence)])                                                  
Out[12]: 6

In [13]: # Another way                                                                                        

In [14]: sum(map(lambda s: int(s), re.findall(r'\d+', sentence)))                                             
Out[14]: 6
```
