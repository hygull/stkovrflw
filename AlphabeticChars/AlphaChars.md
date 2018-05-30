**@Kimberly**, as I understood from your code, you want to read a text file of alphabetic characters.
You want to also ignore the cases of alphabetic characters in file. Finally, you want to count the occurences of each unique letters in the text file.

I will suggest you to use **dictionary** for this. I have written a simple code for this task which 
satisfy the following 3 conditions (please comment if you want different result by providing inputs and expected outputs, I will update my code based on that):

> 1. Reads text file and creates a single line of text by removing any spaces in between.
>
> 2. It converts upper case letters to lower case letters.
>
> 3. Finally, it creates a dictionary containing unique letters with their frequencies.

### &raquo; Lateralus.txt

	abcdefghijK
	ABCDEfgkjHI
	IhDcabEfGKJ
	mkmkmkmkmoo
	pkdpkdpkdAB
	A B C D F Q
	ab abc ab c

### &raquo; Code

	import json

	char_occurences = {}

	with open('Lateralus.txt', 'r') as file:
		all_lines_combined = ''.join([line.replace(' ', '').strip().lower() for line in file.readlines()])

	print all_lines_combined # abcdefghijKABCDEfgkjHIIhDcabEfGKJmkmkmkmkmoopkdpkdpkdABABCDFQababcabc
	print len(all_lines_combined) # 69 (7 lines of 11 characters, 8 spaces => 77-8 = 69)

	while all_lines_combined:
		ch = all_lines_combined[0]

		char_occurences[ch] = all_lines_combined.count(ch)

		all_lines_combined = all_lines_combined.replace(ch, '') 

	# Pretty printing char_occurences dictionary containing occurences of 
	# alphabetic characters in a text file

	print json.dumps(char_occurences, indent=4)

	"""
		{
		    "a": 8,
		    "c": 6,
		    "b": 8,
		    "e": 3,
		    "d": 7,
		    "g": 3,
		    "f": 4,
		    "i": 3,
		    "h": 3,
		    "k": 10,
		    "j": 3,
		    "m": 5,
		    "o": 2,
		    "q": 1,
		    "p": 3
		}
	"""