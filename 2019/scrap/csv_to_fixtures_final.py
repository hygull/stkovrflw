import glob
import pandas as pd
import re
import json
import copy

pk = 1
csv_paths = glob.glob("./csvs/*.csv")
print(csv_paths)

# Processing => 232 ./csvs/IFCB2009_197.csv
# Index(['Unnamed: 0', 'BANK NAME', 'IFSC', 'OFFICE', 'ADDRESS', 'DISTRICT',
#        'CITY', 'STATE', 'PHONE'],
#       dtype='object')
# Processing => 233 ./csvs/IFCB2009_183.csv
# Index(['Unnamed: 0', 'BANK', 'IFSC', 'MICR', 'BRANCH', 'ADDRESS', 'CONTACT',
#        'CITY', 'DISTRICT', 'STATE'],
# print("Column names: ", columns)

columns = ["bank_name", "branch", "state", "address", "ifsc", "city", "district", "office", "phone"]
csv_paths = enumerate(csv_paths)
idx, csv_path = csv_paths.__next__()
idx += 1
include = True
key = ''
model_fields = {
	"bank_name": '',
	"ifsc": '',
	"city": '',
	"branch": '',
	"district": "",
	"phone": '',
	"state": '',
	"address": '',
	"office": '' 
}
initial_fields = {"model": "masterdata.ifscnew"}

with open("exception4.txt", "a+")  as fa, open("rows.txt", "a+") as fe:
	while True:
		try:
			rows = []
			# print("---" * 20)
			print("Processing =>", idx, csv_path)
			# print("---" * 20)

			df = pd.read_csv(csv_path)	
			df.columns = [column.strip() for column in df.columns]
			d = initial_fields.copy()
			# d = copy.deepcopy(initial_fields)
			for index, row in df.iterrows():
				d["pk"] = pk

				# class IFSC(models.Model):
				#     bank_name = models.CharField(max_length=128)
				#     ifsc = models.CharField(max_length=128)
				#     city = models.CharField(max_length=128, null=True)
				#     branch = models.CharField(max_length=128, null=True)
				#     district = models.CharField(max_length=128, null=True)
				#     state = models.CharField(max_length=128, null=True)
				#     phone = models.CharField(max_length=128, null=True)
				#     address = models.TextField(blank=True, null=True)
				fields = model_fields.copy()
				# fields = copy.deepcopy(model_fields)
				# print("@@@" * 20, id(fields))

				# print("Columns => ", df.columns)
				for i, column in enumerate(df.columns):
					# print("---" * 20)
					# print("Column => ", column)

					# column = column.strip()

					include = True
					if column in ["BANK", "BANK NAME"]:
						# print("--1--")
						key = "bank_name"
					elif column in ["IFSC"]:
						# print("--2--")
						key = "ifsc"
					elif column in ["CITY"]:
						# print("--3--")
						key = "city"
					elif column in ["BRANCH"]:
						# print("--4--")
						key = "branch"
					elif column in ["DISTRICT"]:
						# print("--5--")
						key = "district"
					elif column in ["CONTACT", "PHONE"]:
						# print("--6--")
						key = "phone"
					elif column in ["STATE"]:
						# print("--7--")
						key = "state"
					elif column in ["ADDRESS"]:
						# print("--8--")
						key = "address"
					elif column in ["OFFICE"]:
						# print("--9--")
						key = "office"
					else:
						include = False

					# print("include", include, key)
					if include:
						print("row[column]", row[column])
						fields[key] = str(row[column]) # for phone (it is integer)

					# print("key", key, " ===> ", fields)
					# print("---" * 20)

				d["fields"] = fields
				# print("fields =>", fields)
				rows.append({**d})
				fe.write(str(len(rows)) + "\n")
				pk += 1
				if not include:
					fa.write("Invalid Columns => " + str(i) + " - " + column)
				# break

			json_file_name = csv_path.lstrip("./csvs").rstrip(".csv") + ".json"
			# print("JSON file path =>" + json_file_name)
			# FileNotFoundError: [Errno 2] No such file or directory: './fixtures//csvs/IFCB2009_183.csv.json'

			# >>> import glob
			# >>> glob.glob("./*.py")
			# ['./csv_to_fixtures.py', './ifsc_rbi.py', './ifsc_rbi_2nd.py', './ifsc_rbi_pandas_3rd.py']
			# >>> 
			with open("./fixtures_new/" + json_file_name, "w") as fw:
				fw.write(json.dumps(rows, indent=4, sort_keys=True))
				print( json_file_name + " saved")

			idx, csv_path = csv_paths.__next__()
			idx += 1
			# for i in rows:
			# 	print(id(i))
			# break
		except StopIteration as error:
			print("\nSuccessful")
			break
		except Exception as error:
			import traceback
			import sys
			exc_type, exc_value, exc_traceback = sys.exc_info()
			traceback.print_tb(exc_traceback, limit=200, file=sys.stdout)
			print(error)
			fa.write(str(idx) + "--" + str(idx) +  "--" + str(error) + "--" + csv_path + "\n")
			idx, csv_path = csv_paths.__next__()
			idx += 1
			break
