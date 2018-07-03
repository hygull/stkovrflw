**in** is a membership operator is Python. It is used to check the membership of any item inside the whole collection (`list`, `tuple`, `dictionary`, `set` etc.).

In your case you are checking for the membership of an item `('Jose', 6)` for a complete iteration over dictionary `my_friends` and in each iteration it is `True` because of True membership (i.e. the item `('Jose', 6)` is a member of `my_friends`).

> **Note:** It does not matter how many times you're checking for the membership of same item inside collection.

Have a look at the below example.

    >>> l = [1, 2, 3, 4, 5, 6]
    >>>
    >>> for item in l:
    ...     if 1 in l:
    ...         print('yes');
    ...
    yes
    yes
    yes
    yes
    yes
    yes
    >>>
    >>> 2 in l
    True
    >>>
    >>> 7 in l
    False
    >>>
    >>> # Dictinary example
    ...
    >>> d = {'a': 1, 'b': 2, 'c': 3}
    >>>
    >>> d.items()
    dict_items([('a', 1), ('b', 2), ('c', 3)])
    >>>
    >>> list(d.items())
    [('a', 1), ('b', 2), ('c', 3)]
    >>>
    >>> ('a', 1) in d.items()
    True
    >>> ('a', 4) in d.items()
    False
    >>>

&nbsp; **Better solution** is to make your program like this:

    >>> a = ('Jose', 6)
    >>> for e, v in my_friends.items():
    ...     if a == (e, v):
    ...         print('yes');
    ...
    yes
    >>>