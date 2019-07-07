# class Vendor(BusinessPeople):
# 	shop_name = models.CharField(max_length=50, null=False, blank=False)
# 	shop_address = models.TextField()


# class Customer(BusinessPeople):
# 	delivery_address = models.TextField()


# class Product(models.Model):
# 	name = models.CharField(max_length=50, blank=False, null=False)
# 	url = models.URLField(max_length=1000, blank=False, null=False)
# 	price = models.PositiveIntegerField(blank=False, null=False)
# 	vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)
	
# 	def __unicode__(self):
# 		return self.name

'''abcdefghijklmn
<entry colname="1" rowname="1">a</entry>
<entry morecols="5" morecolname="2" namest="2" nameend="7" rowname="1">a</entry>TEST
<entry colname="1" morerows="9" morerowname="2">b</entry>
<entry morecols="5" morecolname="2" namest="2" nameend="7" rowname="2">b</entry>
<entry colname="1" morerows="9" morerowname="2">b</entry>TEST
<morecols="4" morecolname="3" namest="3" nameend="7" morerows="2" morerowname="3">c</entry>
<entry colname="2" rowname="3">c</entry>TEST
<entry colname="2" rowname="4">d</entry>TEST
<entry morecols="1" morecolname="2" namest="2" nameend="3" morerows="2" morerowname="5">e</entry>
<entry colname="2" rowname="5">e</entry>TEST
abcdefghijklmn'''

import re

# Reading XML file 
with open("C:\\TEST\\test1.xml", "r") as f:
# with open("C:\\TEST\\test_addrow.xml", "r") as f:
    lines = f.readlines()

last_num = ""
last_index = 0
opened = False

for i, line in enumerate(lines):
	arr = re.findall(r"rowname=\"\d+", line)
	arr2 = []
	if arr:
		arr2 = arr[0].split('"')

	if arr2:
		if last_num and last_num != arr2[1]:
			lines[last_index] = lines[last_index].strip() + 'TEST' + '\n'
			opened = False
		else:
			opened = True

		last_index = i
		last_num = arr2[1]
	else:
		if last_index:
			lines[last_index] = lines[last_index].strip() + 'TEST' + '\n'
			opened = False

if opened:
	lines[last_index] = lines[last_index].strip() + 'TEST' + '\n'

lines = "".join(lines)
print(lines)

# Writing modified lines to file
# with open("C:\\TEST\\test_addrow.xml", "w", encoding='utf-8') as f:
with open("C:\\TEST\\test2.xml", "w") as f:
# with open("C:\\TEST\\test_addrow2.xml", "w") as f:
    f.write(lines)

'''abcdefghijklmn
<entry colname="1" rowname="1">a</entry>
<entry morecols="5" morecolname="2" namest="2" nameend="7" rowname="1">a</entry>TEST
<entry colname="1" morerows="9" morerowname="2">b</entry>
<entry morecols="5" morecolname="2" namest="2" nameend="7" rowname="2">b</entry>
<entry colname="1" morerows="9" morerowname="2">b</entry>TEST
<morecols="4" morecolname="3" namest="3" nameend="7" morerows="2" morerowname="3">c</entry>
<entry colname="2" rowname="3">c</entry>TEST
<entry colname="2" rowname="4">d</entry>TEST
<entry morecols="1" morecolname="2" namest="2" nameend="3" morerows="2" morerowname="5">e</entry>
<entry colname="2" rowname="5">e</entry>TEST
abcdefghijklmn'''
