Try to set the below 2 options.

+ `pd.set_option("display.max_columns", df.columns.shape[0])`

+ `pd.set_option("display.max_rows", df.index.shape[0])`


I have presented a simple example below, it may help you to fix this. Just have a look at it, understand and try.

    >>> import pandas as pd
    >>> 
    >>> d = {
    ...     "fullname": ["R A", "X Y", "P K", "X Y", "D R", "R A", "R E", "X Y"],
    ...     "age": [26, 25, 50, 34, 67, 89, 50, 26],
    ...     "profession": ["Python Developer", "Node Developer", "Django Developer", "JS Developer", "Python Developer", "Node Developer", "Node Developer", "Python Developer"]
    ... }
    >>> 
    >>> df = pd.DataFrame(d)
    >>> df
      fullname  age        profession
    0      R A   26  Python Developer
    1      X Y   25    Node Developer
    2      P K   50  Django Developer
    3      X Y   34      JS Developer
    4      D R   67  Python Developer
    5      R A   89    Node Developer
    6      R E   50    Node Developer
    7      X Y   26  Python Developer
    >>> 
    >>> group1 = df.groupby("fullname")
    >>> group2 = df.groupby("age")
    >>> group3 = df.groupby("profession")
    >>> 
    >>> group1
    <pandas.core.groupby.groupby.DataFrameGroupBy object at 0x101209a90>
    >>> 
    >>> group1.groups
    {'D R': Int64Index([4], dtype='int64'), 'P K': Int64Index([2], dtype='int64'), 'R A': Int64Index([0, 5], dtype='int64'), 'R E': Int64Index([6], dtype='int64'), 'X Y': Int64Index([1, 3, 7], dtype='int64')}
    >>> 
    >>> group1.get_group("R A")
      fullname  age        profession
    0      R A   26  Python Developer
    5      R A   89    Node Developer
    >>> 
    >>> group1.get_group("R E")
      fullname  age      profession
    6      R E   50  Node Developer
    >>> 
    >>> group1.get_group("P K")
      fullname  age        profession
    2      P K   50  Django Developer
    >>> 
    >>> for group in group1.groups:
    ...     print(group)
    ... 
    D R
    P K
    R A
    R E
    X Y
    >>> for group in group1.groups:
    ...     print(group1.get_group(group))
    ... 
      fullname  age        profession
    4      D R   67  Python Developer
      fullname  age        profession
    2      P K   50  Django Developer
      fullname  age        profession
    0      R A   26  Python Developer
    5      R A   89    Node Developer
      fullname  age      profession
    6      R E   50  Node Developer
      fullname  age        profession
    1      X Y   25    Node Developer
    3      X Y   34      JS Developer
    7      X Y   26  Python Developer
    >>> 
    >>> group1.get_group("R A")
      fullname  age        profession
    0      R A   26  Python Developer
    5      R A   89    Node Developer
    >>> 
    >>> pd.set_option("display.max_columns", 2)
    >>> group1.get_group("R A")
      fullname        ...               profession
    0      R A        ...         Python Developer
    5      R A        ...           Node Developer

    [2 rows x 3 columns]
    >>> 
    >>> ra_group = group1.get_group("R A")
    >>> ra_columns = ra_group.columns
    >>> ra_columns
    Index(['fullname', 'age', 'profession'], dtype='object')
    >>> 
    >>> ra_columns.ndim
    1
    >>> ra_columns.size
    3
    >>> ra_columns.shape
    (3,)
    >>> 
    >>> pd.set_option("display.max_columns", ra_columns.shape[0])
    >>> group1.get_group("R A")
      fullname  age        profession
    0      R A   26  Python Developer
    5      R A   89    Node Developer
    >>> 
    >>> ra_group
      fullname  age        profession
    0      R A   26  Python Developer
    5      R A   89    Node Developer
    >>> 
    >>> ra_group.index
    Int64Index([0, 5], dtype='int64')
    >>> 
    >>> ra_group.index.shape
    (2,)
    >>> pd.set_option("display.max_rows", ra_group.index.shape[0])
    >>> ra_group
      fullname  age        profession
    0      R A   26  Python Developer
    5      R A   89    Node Developer
    >>>
    >>> pd.set_option("display.max_rows", ra_group.index.shape[0] - 1)
    >>> ra_group
       fullname  age        profession
    0       R A   26  Python Developer
    ..      ...  ...               ...

    [2 rows x 3 columns]
    >>> 