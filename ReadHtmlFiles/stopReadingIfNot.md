I'll suggest you to use **os.path.exists()** `(which returns True/False)` and **os.path.isfile()** both.

Use **with** statement to open file. It is **Pythonic way** to open files.

> **with** statement is best preferred among the professional coders.

These are the contents of my current working directory.

	H:\RishikeshAgrawani\Projects\Stk\ReadHtmlFiles>dir
	 Volume in drive H is New Volume
	 Volume Serial Number is C867-828E

	 Directory of H:\RishikeshAgrawani\Projects\Stk\ReadHtmlFiles

	11/05/2018  16:12    <DIR>          .
	11/05/2018  16:12    <DIR>          ..
	11/05/2018  15:54               106 source1.html
	11/05/2018  15:54               106 source2.html
	11/05/2018  15:54               106 source3.html
	11/05/2018  16:12                 0 stopReadingIfNot.md
	11/05/2018  16:11               521 stopReadingIfNot.py
	               5 File(s)            839 bytes
	               2 Dir(s)  196,260,925,440 bytes free

The below Python code shows how will you read files source1.html, source2.html, source.3.html and stop if there is no more files of the form sourceX.html (where X is 1, 2, 3, 4, ... etc.).

## Sample code:

	import os

	n = 1;
	html_file_name = 'source%d.html'

	# It is necessary to check if sourceX.html is file or directory.
	# If it is directory the check it if it exists or not.
	# It it exists then perform operation (read/write etc.) on file.
	while os.path.isfile(html_file_name % (n)) and os.path.exists(html_file_name % (n)):
		print "Reading ", html_file_name % (n)

		# The best way (Pythonic way) to open file
		# You don't need to bother about closing the file
		# It will be taken care by with statement
		with open(html_file_name % (n), "r") as file:
			# Make sure it works
			print html_file_name % (n), " exists\n"; 

		n += 1;


## Output:

	H:\RishikeshAgrawani\Projects\Stk\ReadHtmlFiles>python stopReadingIfNot.py
	Reading  source1.html
	source1.html  exists

	Reading  source2.html
	source2.html  exists

	Reading  source3.html
	source3.html  exists

So based on the above logic. you can modify your code. It will work.

Thanks.