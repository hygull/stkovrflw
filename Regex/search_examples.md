# re.search() example

```python
In [16]: import re                                                                                             

In [17]: sentence = "This year is the 1 among past 2 years with similar experice I had in 3rd of march"       

In [18]: re.search(r'\d+', sentence).start                                                                    
Out[18]: <function SRE_Match.start(group=0, /)>

In [19]: re.search(r'\d+', sentence).start()                                                                  
Out[19]: 17

In [20]: re.search(r'\d+', sentence), re.search(r'\d+', sentence).end()                                       
Out[20]: (<_sre.SRE_Match object; span=(17, 18), match='1'>, 18)

In [21]: re.search(r'\d+', sentence).start(), re.search(r'\d+', sentence).end()                               
Out[21]: (17, 18)

In [22]: start, end = re.search(r'\d+', sentence).start(), re.search(r'\d+', sentence).end()                  

In [23]: sentence[17:18]                                                                                      
Out[23]: '1'

In [24]: re.search(r'\d+', sentence).groups()                                                                 
Out[24]: ()

In [27]: re.search(r'\d+', sentence).pos                                                                      
Out[27]: 0

In [28]: re.search(r'\d+', sentence).string                                                                   
Out[28]: 'This year is the 1 among past 2 years with similar experice I had in 3rd of march'

In [29]:         
```