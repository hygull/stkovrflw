[https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_69.xlsx](https://rbidocs.rbi.org.in/rdocs/Content/DOCs/IFCB2009_69.xlsx)

```bash
DataFrame Excel Path =>/Users/hygull/Projects/Python3/stkovrflw/2019/scrap/xlsx_files5/IFCB2009_69.xlsx
Traceback (most recent call last):
  File "ifsc_rbi_pandas_3rd.py", line 102, in <module>
    df = pd.read_excel(os.path.join(os.path.abspath("."), "xlsx_files5", file_name))
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/util/_decorators.py", line 178, in wrapper
    return func(*args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/util/_decorators.py", line 178, in wrapper
    return func(*args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/io/excel.py", line 307, in read_excel
    io = ExcelFile(io, engine=engine)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/pandas/io/excel.py", line 394, in __init__
    self.book = xlrd.open_workbook(self._io)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/xlrd/__init__.py", line 441, in open_workbook
    ragged_rows=ragged_rows,
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/xlrd/book.py", line 91, in open_workbook_xls
    biff_version = bk.getbof(XL_WORKBOOK_GLOBALS)
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/xlrd/book.py", line 1230, in getbof
    bof_error('Expected BOF record; found %r' % self.mem[savpos:savpos+8])
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/xlrd/book.py", line 1224, in bof_error
    raise XLRDError('Unsupported format, or corrupt file: ' + msg)
```