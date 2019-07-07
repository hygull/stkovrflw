```bash
>>> class A(object):
...     pass
... 
>>> class B(object):
...     pass
... 
>>> class C(A, B):
...     pass
... 
>>> class D(B, A):
...     pass
... 
>>> class D(B, A):
...     pass
... 
>>> A.__mro__
(<class '__main__.A'>, <class 'object'>)
>>> 
>>> B.__mro__
(<class '__main__.B'>, <class 'object'>)
>>> 
>>> C.__mro__
(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
```

```bash
>>> class A:
...     def __init__(self):
...         print('INIT')
...     @staticmethod
...     def p(ok):
...         print(ok, ' bye')
... 
>>> A.p(1)
1  bye
>>> 
>>> class B:
...     def __init__(self):
...         print('INIT')
...     @classmethod
...     def p(cls, ok):
...         cls()
...         print(ok)
... 
>>> B.p(34)
INIT
34
>>> 

```