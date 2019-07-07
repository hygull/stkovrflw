# https://stackoverflow.com/questions/50678599/how-to-merge-two-irregular-data-frames-in-python/50679950#50679950
import pandas as pd
import numpy as np 

data_arr1 = [
	['A', '1-3', 5],
	['',  '4-7', 23],
	['',  '8-15', 2],
	['B', '4-7', 4],
	['', '8-15', 1],
	['C', '1-3', 5],
	['D', '1-3', 2],
	['E', '1-3', 9]
]
columns1 = ["Car", "Range(Days)", "Sold"];

data_arr2 = [
	['A', 2],
	['C', 45],
	['D', 32],
	['E', 1]
];
columns2 = ["Car", "Repair_Calls"];

# Creating DataFrames
df = pd.DataFrame(data_arr1, columns=columns1)
df2 = pd.DataFrame(data_arr2, columns=columns2)

# Printing Dataframes
print(df);
print('\n')
print(df2);

# Merging df & df2 to get desired output
df3 = pd.merge(left=df, right=df2, left_on="Car", right_on="Car", how="outer").replace(np.nan, "", regex=True)
print('\n')
print(df3)

### Output &raquo;
"""
	  Car Range(Days)  Sold
	0   A         1-3     5
	1             4-7    23
	2            8-15     2
	3   B         4-7     4
	4            8-15     1
	5   C         1-3     5
	6   D         1-3     2
	7   E         1-3     9


	  Car  Repair_Calls
	0   A             2
	1   C            45
	2   D            32
	3   E             1


	  Car Range(Days)  Sold Repair_Calls
	0   A         1-3     5            2
	1             4-7    23
	2            8-15     2
	3            8-15     1
	4   B         4-7     4
	5   C         1-3     5           45
	6   D         1-3     2           32
	7   E         1-3     9            1
"""