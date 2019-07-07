import os
import codecs

def create_text_file(forder_path, count):
	for i in range(count): 
		name = "{}.txt".format(i + 1)
		text_file = os.path.join(forder_path, name)

		with codecs.open(text_file, "w", encoding="UTF-8") as file:
			contents = file.write('I am learning Python') # Add lines to be written in newly created file
			print('Contents', contents)
		# pass

count = int(input("Nhap count:"))
# create_text_file("C:/Users/Kuem/Desktop/Truyen/Text1", count)

create_text_file("/Users/hygull/Projects/Python3/practice/tuan_problem", count)
