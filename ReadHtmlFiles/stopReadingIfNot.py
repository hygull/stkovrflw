"""
	{
		'aim': 'Stop reading HTML files of the form source1.html, source2.html ... etc.'
	}
"""

import os

n = 1;
html_file_name = 'source%d.html'

while os.path.isfile(html_file_name % (n)) and os.path.exists(html_file_name % (n)):
	print "Reading ", html_file_name % (n)

	# The best way (Pythonic way) to open file
	# You don't need to bother about closing the file
	# It will be taken care by with statement
	with open(html_file_name % (n), "r") as file:
		# Make sure it works
		print html_file_name % (n), " exists\n"; 

	n += 1;
