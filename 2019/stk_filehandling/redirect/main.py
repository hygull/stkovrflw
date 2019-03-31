import os

f=open("pr1.txt","r")

df=0

for i in f:
	print("ikdkd", i)
	df=df+1
	if df==4:
		break
	print i

# os.system("udstask expireimage -image" + i)