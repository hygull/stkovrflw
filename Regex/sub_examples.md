# re.sub() examples

```python
In [1]: import re                                                                                             

In [2]: sentence = 'This is 1 of the powerful place to see all the places of world, do you like it?'          

In [3]: re.sub(r'1', 'one', sentence)                                                                         
Out[3]: 'This is one of the powerful place to see all the places of world, do you like it?'

In [4]: # Example 2                                                                                           

In [5]: sentence2 = "This is   nice one. What do you  think about it?  Thank you.  "                          

In [6]: re.sub(r'\s+', ' ', sentence2).strip()                                                                
Out[6]: 'This is nice one. What do you think about it? Thank you.'
```