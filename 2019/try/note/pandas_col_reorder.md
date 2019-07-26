> https://stackoverflow.com/questions/13148429/how-to-change-the-order-of-dataframe-columns

11 July 2019

```python
>>> import pandas as pd
>>> 
>>> 
>>> df = pd.DataFrame({
...     "iin": [12, 3, 4, 5,22],
...     "pan": ['ss', 'dd', 'ee', 'ww', 'rr'],
...     "name": ["r a", 'r t', 'g t', 'e w', 'o p']
... })
>>> 
>>> df
   iin pan name
0   12  ss  r a
1    3  dd  r t
2    4  ee  g t
3    5  ww  e w
4   22  rr  o p
>>> 
>>> 
>>> df['iin']
0    12
1     3
2     4
3     5
4    22
Name: iin, dtype: int64
>>> 
>>> df['pan']
0    ss
1    dd
2    ee
3    ww
4    rr
Name: pan, dtype: object
>>> df['name']
0    r a
1    r t
2    g t
3    e w
4    o p
Name: name, dtype: object
>>> 
>>> 
>>> df2 = pd.DataFrame()
>>> 
>>> df2
Empty DataFrame
Columns: []
Index: []
>>> 
>>> 
>>> df2['name'] = df['name']
>>> df2
  name
0  r a
1  r t
2  g t
3  e w
4  o p
>>> 
>>> df2['iin'] = df['iin']
>>> df2
  name  iin
0  r a   12
1  r t    3
2  g t    4
3  e w    5
4  o p   22
>>> 
>>> df2['name'] = df['name']
>>> 
>>> df2
  name  iin
0  r a   12
1  r t    3
2  g t    4
3  e w    5
4  o p   22
>>> 
>>> df2['pan'] = df['pan']
>>> 
>>> df2
  name  iin pan
0  r a   12  ss
1  r t    3  dd
2  g t    4  ee
3  e w    5  ww
4  o p   22  rr
>>> 
>>> df
   iin pan name
0   12  ss  r a
1    3  dd  r t
2    4  ee  g t
3    5  ww  e w
4   22  rr  o p
>>> 
>>> df.columns
Index(['iin', 'pan', 'name'], dtype='object')
>>> 
>>> df.columns.tolist()
['iin', 'pan', 'name']
>>> 
>>> 
>>> l = df.columns.tolist()[::-1]
>>> 
>>> df = df[l]
>>> df
  name pan  iin
0  r a  ss   12
1  r t  dd    3
2  g t  ee    4
3  e w  ww    5
4  o p  rr   22
>>> 
```


```python
>>> df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 3 columns):
name    5 non-null object
pan     5 non-null object
iin     5 non-null int64
dtypes: int64(1), object(2)
memory usage: 200.0+ bytes
>>> 
>>> df.columns
Index(['name', 'pan', 'iin'], dtype='object')
>>> 
>>> df.columns.tolist()
['name', 'pan', 'iin']
>>> 
>>> dir(df)
['T', '_AXIS_ALIASES', '_AXIS_IALIASES', '_AXIS_LEN', '_AXIS_NAMES', '_AXIS_NUMBERS', '_AXIS_ORDERS', '_AXIS_REVERSED', '_AXIS_SLICEMAP', '__abs__', '__add__', '__and__', '__array__', '__array_wrap__', '__bool__', '__bytes__', '__class__', '__contains__', '__copy__', '__deepcopy__', '__delattr__', '__delitem__', '__dict__', '__dir__', '__div__', '__doc__', '__eq__', '__finalize__', '__floordiv__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__iand__', '__ifloordiv__', '__imod__', '__imul__', '__init__', '__init_subclass__', '__invert__', '__ior__', '__ipow__', '__isub__', '__iter__', '__itruediv__', '__ixor__', '__le__', '__len__', '__lt__', '__matmul__', '__mod__', '__module__', '__mul__', '__ne__', '__neg__', '__new__', '__nonzero__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmatmul__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__setitem__', '__setstate__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__unicode__', '__weakref__', '__xor__', '_accessors', '_add_numeric_operations', '_add_series_only_operations', '_add_series_or_dataframe_operations', '_agg_by_level', '_agg_doc', '_aggregate', '_aggregate_multiple_funcs', '_align_frame', '_align_series', '_box_col_values', '_box_item_values', '_builtin_table', '_check_inplace_setting', '_check_is_chained_assignment_possible', '_check_label_or_level_ambiguity', '_check_percentile', '_check_setitem_copy', '_clear_item_cache', '_clip_with_one_bound', '_clip_with_scalar', '_combine_const', '_combine_frame', '_combine_match_columns', '_combine_match_index', '_compare_frame', '_consolidate', '_consolidate_inplace', '_construct_axes_dict', '_construct_axes_dict_for_slice', '_construct_axes_dict_from', '_construct_axes_from_arguments', '_constructor', '_constructor_expanddim', '_constructor_sliced', '_convert', '_count_level', '_create_indexer', '_cython_table', '_deprecations', '_dir_additions', '_dir_deletions', '_drop_axis', '_drop_labels_or_levels', '_ensure_valid_index', '_expand_axes', '_find_valid_index', '_from_arrays', '_from_axes', '_get_agg_axis', '_get_axis', '_get_axis_name', '_get_axis_number', '_get_axis_resolvers', '_get_block_manager_axis', '_get_bool_data', '_get_cacher', '_get_index_resolvers', '_get_item_cache', '_get_label_or_level_values', '_get_numeric_data', '_get_value', '_get_values', '_getitem_array', '_getitem_column', '_getitem_frame', '_getitem_multilevel', '_getitem_slice', '_gotitem', '_iget_item_cache', '_indexed_same', '_info_axis', '_info_axis_name', '_info_axis_number', '_info_repr', '_init_dict', '_init_mgr', '_init_ndarray', '_internal_names', '_internal_names_set', '_is_builtin_func', '_is_cached', '_is_copy', '_is_cython_func', '_is_datelike_mixed_type', '_is_label_or_level_reference', '_is_label_reference', '_is_level_reference', '_is_mixed_type', '_is_numeric_mixed_type', '_is_view', '_ix', '_ixs', '_join_compat', '_maybe_cache_changed', '_maybe_update_cacher', '_metadata', '_needs_reindex_multi', '_obj_with_exclusions', '_protect_consolidate', '_reduce', '_reindex_axes', '_reindex_axis', '_reindex_columns', '_reindex_index', '_reindex_multi', '_reindex_with_indexers', '_repr_data_resource_', '_repr_fits_horizontal_', '_repr_fits_vertical_', '_repr_html_', '_repr_latex_', '_reset_cache', '_reset_cacher', '_sanitize_column', '_selected_obj', '_selection', '_selection_list', '_selection_name', '_series', '_set_as_cached', '_set_axis', '_set_axis_name', '_set_is_copy', '_set_item', '_set_value', '_setitem_array', '_setitem_frame', '_setitem_slice', '_setup_axes', '_shallow_copy', '_slice', '_stat_axis', '_stat_axis_name', '_stat_axis_number', '_take', '_to_dict_of_blocks', '_try_aggregate_string_function', '_typ', '_unpickle_frame_compat', '_unpickle_matrix_compat', '_update_inplace', '_validate_dtype', '_values', '_where', '_xs', 'abs', 'add', 'add_prefix', 'add_suffix', 'agg', 'aggregate', 'align', 'all', 'any', 'append', 'apply', 'applymap', 'as_matrix', 'asfreq', 'asof', 'assign', 'astype', 'at', 'at_time', 'axes', 'between_time', 'bfill', 'bool', 'boxplot', 'clip', 'clip_lower', 'clip_upper', 'columns', 'combine', 'combine_first', 'compound', 'copy', 'corr', 'corrwith', 'count', 'cov', 'cummax', 'cummin', 'cumprod', 'cumsum', 'describe', 'diff', 'div', 'divide', 'dot', 'drop', 'drop_duplicates', 'dropna', 'dtypes', 'duplicated', 'empty', 'eq', 'equals', 'eval', 'ewm', 'expanding', 'ffill', 'fillna', 'filter', 'first', 'first_valid_index', 'floordiv', 'from_dict', 'from_records', 'ftypes', 'ge', 'get', 'get_dtype_counts', 'get_ftype_counts', 'get_values', 'groupby', 'gt', 'head', 'hist', 'iat', 'idxmax', 'idxmin', 'iin', 'iloc', 'index', 'infer_objects', 'info', 'insert', 'interpolate', 'isin', 'isna', 'isnull', 'items', 'iteritems', 'iterrows', 'itertuples', 'ix', 'join', 'keys', 'kurt', 'kurtosis', 'last', 'last_valid_index', 'le', 'loc', 'lookup', 'lt', 'mad', 'mask', 'max', 'mean', 'median', 'melt', 'memory_usage', 'merge', 'min', 'mod', 'mode', 'mul', 'multiply', 'name', 'ndim', 'ne', 'nlargest', 'notna', 'notnull', 'nsmallest', 'nunique', 'pan', 'pct_change', 'pipe', 'pivot', 'pivot_table', 'plot', 'pop', 'pow', 'prod', 'product', 'quantile', 'query', 'radd', 'rank', 'rdiv', 'reindex', 'reindex_axis', 'reindex_like', 'rename', 'rename_axis', 'reorder_levels', 'replace', 'resample', 'reset_index', 'rfloordiv', 'rmod', 'rmul', 'rolling', 'round', 'rpow', 'rsub', 'rtruediv', 'sample', 'select', 'select_dtypes', 'sem', 'set_axis', 'set_index', 'shape', 'shift', 'size', 'skew', 'slice_shift', 'sort_index', 'sort_values', 'squeeze', 'stack', 'std', 'style', 'sub', 'subtract', 'sum', 'swapaxes', 'swaplevel', 'tail', 'take', 'to_clipboard', 'to_csv', 'to_dense', 'to_dict', 'to_excel', 'to_feather', 'to_gbq', 'to_hdf', 'to_html', 'to_json', 'to_latex', 'to_msgpack', 'to_panel', 'to_parquet', 'to_period', 'to_pickle', 'to_records', 'to_sparse', 'to_sql', 'to_stata', 'to_string', 'to_timestamp', 'to_xarray', 'transform', 'transpose', 'truediv', 'truncate', 'tshift', 'tz_convert', 'tz_localize', 'unstack', 'update', 'values', 'var', 'where', 'xs']
>>> 
>>> df.to_records
<bound method DataFrame.to_records of   name pan  iin
0  r a  ss   12
1  r t  dd    3
2  g t  ee    4
3  e w  ww    5
4  o p  rr   22>
>>> 
>>> df.to_records
<bound method DataFrame.to_records of   name pan  iin
0  r a  ss   12
1  r t  dd    3
2  g t  ee    4
3  e w  ww    5
4  o p  rr   22>
>>> 
>>> df
  name pan  iin
0  r a  ss   12
1  r t  dd    3
2  g t  ee    4
3  e w  ww    5
4  o p  rr   22
>>> 
>>> df.to_records()
rec.array([(0, 'r a', 'ss', 12), (1, 'r t', 'dd',  3),
           (2, 'g t', 'ee',  4), (3, 'e w', 'ww',  5),
           (4, 'o p', 'rr', 22)],
          dtype=[('index', '<i8'), ('name', 'O'), ('pan', 'O'), ('iin', '<i8')])
>>> 
>>> df.to_records().tolist()
[(0, 'r a', 'ss', 12), (1, 'r t', 'dd', 3), (2, 'g t', 'ee', 4), (3, 'e w', 'ww', 5), (4, 'o p', 'rr', 22)]
>>> 
>>> import json;print(json.dumps(df.to_records().tolist(), indent=4))
[
    [
        0,
        "r a",
        "ss",
        12
    ],
    [
        1,
        "r t",
        "dd",
        3
    ],
    [
        2,
        "g t",
        "ee",
        4
    ],
    [
        3,
        "e w",
        "ww",
        5
    ],
    [
        4,
        "o p",
        "rr",
        22
    ]
]
>>> 
```