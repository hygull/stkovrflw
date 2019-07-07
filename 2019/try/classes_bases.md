```bash
>>> class A:
...     def f(self):
...         print("A")
... 
>>> class B:
...     def f(self):
...         print("B")
... 
>>> 
>>> class C(A, B):
...     pass
... 
>>> class D(B, A):
...     pass
... 
>>> c = C()
>>> c.f()
A
>>> d = D()
>>> d.f()
B
>>> c.__bases__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'C' object has no attribute '__bases__'
>>> 
>>> C.__bases__
(<class '__main__.A'>, <class '__main__.B'>)
>>> 
>>> D.__bases__
(<class '__main__.B'>, <class '__main__.A'>)
>>> 
>>> 
>>> C.__mro__
(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
>>> 
>>> D.__mro__
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
>>> 
```

```bash
>>> class A:
...     pass
... 
>>> a = A()
>>> 
>>> a
<A object at 0x10819b9e8>
>>> 
>>> a.__class__
<class 'A'>
>>> a.__class__.__name__
'A'
>>> b = a.__class__()
>>> b
<A object at 0x10822a0f0>
>>> 
>>> A.__ora__
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: type object 'A' has no attribute '__ora__'
>>> 
>>> dir(A)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
>>> 
>>> A.__mro__
(<class 'A'>, <class 'object'>)
>>> A.__class
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: type object 'A' has no attribute '__class'
>>> 
>>> A.__class__
<class 'type'>
>>> A.__bases__
(<class 'object'>,)
>>> 
>>> class C:
...     pass
... 
>>> class B(A, B):
... 
KeyboardInterrupt
>>> class B(A, C):
...     pass
... 
>>> B.__mro__
(<class 'B'>, <class 'A'>, <class 'C'>, <class 'object'>)
>>> 
>>> 
```