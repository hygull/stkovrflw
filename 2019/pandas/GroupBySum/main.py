import pandas as pd 

df = pd.read_csv("data.csv")
print(df)

df = df.groupby("PatientID").sum()
print(df)