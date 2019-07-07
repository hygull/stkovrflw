
```csv
,BANK NAME,IFSC ,BRANCH,ADDRESS,CITY,DISTRICT,STATE,CONTACT
0,"RESERVE BANK OF INDIA , PAD",RBIS0AGPA01,AGARTALA,"II FLOOR,JACKSON GATE BUILDING LENIN SARANI,AGARTALA",AGARTALA,TRIPURA,TRIPURA,2381051
1,"RESERVE BANK OF INDIA , PAD",RBIS0GSTPMT,RBI NEFT RTGS GST COLLECTION,"ASST. GENERAL MANAGER,GST CELL,RESERVE BANK OF INDIA,MUMBAI REGIONAL OFFICE,FORT,MUMBAI - 400001",MUMBAI,MUMBAI,MAHARASHTRA,22642836
```

```python
column = column.strip()
```

```bash
row[column] RESERVE BANK OF INDIA , PAD
  File "csv_to_fixtures_saved.py", line 106, in <module>
    print("row[column]", row[column])
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/series.py", line 767, in __getitem__
    result = self.index.get_value(self, key)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 3132, in get_value
    raise e1
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/core/indexes/base.py", line 3118, in get_value
    tz=getattr(series.dtype, 'tz', None))
  File "pandas/_libs/index.pyx", line 106, in pandas._libs.index.IndexEngine.get_value
  File "pandas/_libs/index.pyx", line 114, in pandas._libs.index.IndexEngine.get_value
  File "pandas/_libs/index.pyx", line 162, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 1492, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 1500, in pandas._libs.hashtable.PyObjectHashTable.get_item
'IFSC'
```

Do changed to

```python
df.columns = [column.strip() for column in df.columns]


```
