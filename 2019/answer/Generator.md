Once you will 

+ learn/know about how Python generator works

+ write/create your own generators

you will easily figure out this problem (looks strange but very useful and simple).

> Thanks to **yield** keyword & **StopIteration** exception & some magic methods as these play great roles in writing our own generator.

```python
Python 3.6.7 (v3.6.7:6ec5cf24b7, Oct 20 2018, 03:02:14) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> arr = [1729, 67, 92]
>>> gen = map(str, arr)
>>> 
>>> # 1st item
... 
>>> gen.__next__()
'1729'
>>> 
>>> # 2nd item
... 
>>> gen.__next__()
'67'
>>> 
>>> # 3rd item
... 
>>> gen.__next__()
'92'
>>> 
>>> # This will not work (Exception beacause no more items are in generator, over)
... 
>>> gen.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> 
```

So if you will focus on below kind of examples, you will be confused (1st time).

```python
>>> arr2 = list(gen)
>>> arr2
['1729', '67', '92']
>>>
>>> # Generator has already been iterated, so no more items
...
>>> gen.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
>>> arr2 = list(gen)
>>> arr2
[]
>>> 
```

Just for references, have a look at below links.

+ https://www.programiz.com/python-programming/generator

+ https://dbader.org/blog/python-generator-expressions