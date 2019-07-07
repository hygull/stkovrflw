import subprocess
import pandas as pd 

"""
line1 = lines.pop(0)
>>> line1
'USER               PID  %CPU %MEM      VSZ    RSS   TT  STAT STARTED      TIME COMMAND'
>>> 
>>> line1.find("COMMAND")
79
>>> line1[79]
'C'
>>> d = {}
>>> 
>>> for col in columns:
...     d[col] = []
... 
>>> d
{'USER': [], 'PID': [], '%CPU': [], '%MEM': [], 'VSZ': [], 'RSS': [], 'TT': [], 'STAT': [], 'STARTED': [], 'TIME': [], 'COMMAND': []}
>>> 
>>> for line in lines:
...     f, s = line[:79], line[79:]
...     row = f.split()
...     for i, data in enumerate(columns[:-1]):
...         d[data].append(row[i])
...     d["COMMAND"].append(s)
... 
>>> d
"""

output = subprocess.getoutput('ps aux')
lines = output.split('\n')

line1 = lines.pop(0)
print(line1)

i = line1.find("COMMAND")
d = {}

for col in columns:
	d[col] = []


for line in lines:
	f, s = line[:79], line[79:]
	row = f.split()

	for i, data in enumerate(columns[:-1]):
		d[data].append(row[i])

	d["COMMAND"].append(s)

df = pd.DataFrame(d)
print(df)
print(df["PID"])