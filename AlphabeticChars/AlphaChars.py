# lists_of_lines = []
# with open('Lateralus.txt', 'r') as my_file:
#     for line in my_file:
#         chars_in_lines = [char for char in list(line) if char] # Do not include space if it's there
#         lists_of_lines.append(chars_in_lines)

# for i in range(0,len(word)): word[i] = word[i].lower()    

# word.sort()

# for count in word:
#     if count in word:
#        word[count] = word[count] + 1
# else:
#     word[count] = 1

# for  (word,many)  in word.items(): 
#     print('{:20}{:1}'.format(word,many))


"""
--Lateralus.txt--

abcdefghijK
ABCDEfgkjHI
IhDcabEfGKJ
mkmkmkmkmoo
pkdpkdpkdAB
A B C D F Q
ab abc ab c
"""

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
# word = []
# with open('Lateralus.txt', 'r') as my_file:
#     for line in my_file:
#         temporary_holder = line.split()
#         for i in temporary_holder:
#             word.append(i)

# for i in range(0,len(word)): word[i] = word[i].lower()    

# word.sort()

# for count in word:
#     if count in word:
#        word[count] = word[count] + 1
# else:
#     word[count] = 1

# for  (word,many)  in word.items(): 
#     print('{:20}{:1}'.format(word,many))