import glob
import pandas as pd
import re
import json
import copy


def csv_to_fixtures(idx, csv_path):
	# Processing => 232 ./csvs/IFCB2009_197.csv
	# Index(['Unnamed: 0', 'BANK NAME', 'IFSC', 'OFFICE', 'ADDRESS', 'DISTRICT',
	#        'CITY', 'STATE', 'PHONE'],
	#       dtype='object')
	# Processing => 233 ./csvs/IFCB2009_183.csv
	# Index(['Unnamed: 0', 'BANK', 'IFSC', 'MICR', 'BRANCH', 'ADDRESS', 'CONTACT',
	#        'CITY', 'DISTRICT', 'STATE'],
	# print("Column names: ", columns)

	columns = ["bank_name", "branch", "state", "address", "ifsc", "city", "district", "office", "phone"]
	# csv_paths = enumerate(csv_paths)
	# idx, csv_path = csv_paths.__next__()
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
	initial_fields = {"model": "masterdata.ifsc"}

	rows = []
	print("---" * 20)
	print("Processing =>", idx, csv_path)
	print("---" * 20)

	df = pd.read_csv(csv_path)
	if idx == 1:
		print(df)
		print("---" * 20)

	if idx == 1:
		print(df)
		print("---" *20)	

	# d = initial_fields.copy()
	# d = copy.deepcopy(initial_fields)
	d = {"model": "masterdata.ifsc"}
	for index, row in df.iterrows():
		d["pk"] = index + 1
		print("*" * 60)
		print(index, "\n", row, "\n", id(d))
		print("*" * 60)

		# class IFSC(models.Model):
		#     bank_name = models.CharField(max_length=128)
		#     ifsc = models.CharField(max_length=128)
		#     city = models.CharField(max_length=128, null=True)
		#     branch = models.CharField(max_length=128, null=True)
		#     district = models.CharField(max_length=128, null=True)
		#     state = models.CharField(max_length=128, null=True)
		#     phone = models.CharField(max_length=128, null=True)
		#     address = models.TextField(blank=True, null=True)
		# fields = model_fields.copy()
		# fields = copy.deepcopy(model_fields)

		fields = {
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
		print("@@@" * 20, id(fields))

		print("Columns => ", df.columns)
		for i, column in enumerate(df.columns):
			print("---" * 20)
			print("Column => ", column)

			column = column.strip()

			include = True
			if column in ["BANK", "BANK NAME"]:
				print("--1--")
				key = "bank_name"
			elif column in ["IFSC"]:
				print("--2--")
				key = "ifsc"
			elif column in ["CITY"]:
				print("--3--")
				key = "city"
			elif column in ["BRANCH"]:
				print("--4--")
				key = "branch"
			elif column in ["DISTRICT"]:
				print("--5--")
				key = "district"
			elif column in ["CONTACT", "PHONE"]:
				print("--6--")
				key = "phone"
			elif column in ["STATE"]:
				print("--7--")
				key = "state"
			elif column in ["ADDRESS"]:
				print("--8--")
				key = "address"
			elif column in ["OFFICE"]:
				print("--9--")
				key = "office"

			print("include", include, key)
			if include:
				fields[key] = row[column]


			# print("key", key, " ===> ", fields)
			# print("---" * 20)

			print("------* ROWS *--------")
			print(rows)

		d["fields"] = fields
		print("fields =>", fields)
		rows.append({**d})
		# del fields
		# del d
		# break

		json_file_name = csv_path.lstrip("./csvs").rstrip(".csv") + ".json"
		print("JSON file path =>" + json_file_name)
		# FileNotFoundError: [Errno 2] No such file or directory: './fixtures//csvs/IFCB2009_183.csv.json'

		
		# >>> import glob
		# >>> glob.glob("./*.py")
		# ['./csv_to_fixtures.py', './ifsc_rbi.py', './ifsc_rbi_2nd.py', './ifsc_rbi_pandas_3rd.py']
		# >>> 
		with open("./fixtures/" + json_file_name, "w") as fw:
			fw.write(json.dumps(rows, indent=4, sort_keys=True))
			print( json_file_name + " saved")

		# 	idx, csv_path = csv_paths.__next__()
		# 	idx += 1
		# 	for i in rows:
		# 		print(id(i))
		# 	break
		# except StopIteration as error:
		# 	print("\nSuccessful")
		# 	break
		# except Exception as error:
		# 	fa.write(str(idx) + "--" + str(idx) +  "--" + str(error) + "--" + csv_path + "\n")
		# 	idx, csv_path = csv_paths.__next__()
		# 	idx += 1

def start():
	while True:
		with open("exceptions3.txt", "a+") as fa:
			try:
				csv_paths = glob.glob("./csvs/*.csv")
				print(csv_paths)

				csv_paths = enumerate(csv_paths)
				idx, csv_path = csv_paths.__next__()

				print(idx, csv_path)
				csv_to_fixtures(idx, csv_path)
					# FileNotFoundError: [Errno 2] No such file or directory: './fixtures//csvs/IFCB2009_183.csv.json'

				# >>> import glob
				# >>> glob.glob("./*.py")
				# ['./csv_to_fixtures.py', './ifsc_rbi.py', './ifsc_rbi_2nd.py', './ifsc_rbi_pandas_3rd.py']
				# >>> 

				idx, csv_path = csv_paths.__next__()
				idx += 1
				# for i in rows:
				# 	print(id(i))
				break
			except StopIteration as error:
				print("\nSuccessful")
				break
			except Exception as error:
				fa.write(str(idx) + "--" + str(idx) +  "--" + str(error) + "--" + csv_path + "\n")
				idx, csv_path = csv_paths.__next__()
				idx += 1

				print("Exception", error)
				break

start()
