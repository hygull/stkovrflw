# https://stackoverflow.com/questions/51380591/read-selected-rows-and-columns-based-on-user-input

# >>> import numpy as np
# >>> arr5x5 = np.random.randint(low=-10, high=-5, size=(5, 3))
# >>> arr5x5
# array([[-10,  -8,  -8],
#        [ -9,  -9,  -7],
#        [ -8,  -8, -10],
#        [ -9,  -6,  -7],
#        [ -7,  -7,  -7]])
# >>> import pandas as pd
# >>> df = pd.DataFrame(arr5x5, index=['a', 'b', 'c', 'D', 'e'], columns=['A', 'D', 'E'])
# >>> df
#     A  D   E
# a -10 -8  -8
# b  -9 -9  -7
# c  -8 -8 -10
# D  -9 -6  -7
# e  -7 -7  -7
# >>> df.min()
# A   -10
# D    -9
# E   -10
# dtype: int32
# >>>
# >>> df2 = df.min()
# >>> df2
# A   -10
# D    -9
# E   -10
# dtype: int32
# >>>
# >>> type(df2)
# <class 'pandas.core.series.Series'>
# >>>
# >>> df2[0]
# -10
# >>> df2[1]
# -9
# >>> df2[2]
# -10
# >>> df2['A']
# -10
# >>> df2['D']
# -9
# >>> df2['E']
# -10
# >>>


import numpy as np
import pandas as pd 

# READ FILE AND STORE THE DATA IN 2D LIST
data_list = [] # FUTURE'S 2D LIST

with open('data.txt') as f:
	lines = f.readlines()[2:]
	for line in lines:
		arr = [float(num) for num in line.split()[1:]]
		data_list.append(arr)

# PRINT 2D LIST
print data_list, '\n'

# Column names (I assume list)
column_names = None
row_names = None
if data_list:
	column_names = ['Col'+ str(i) for i in range(1, len(data_list[0])+1)]
	row_names = ['Row' + str(i) for i in range(1, len(data_list)+1)] 

# CREATING DataFrame FROM 2D LIST
df = pd.DataFrame(data_list, columns=column_names, index=row_names)

# PRINT DataFrame
print df, '\n'

# GET MINIMUM OF ALL COLUMNS AS panda's Series
mins = df.min()

# PRINT mins Series
print mins, '\n'