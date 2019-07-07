"""
	StkOvrFlw link: https://stackoverflow.com/questions/50485559/how-to-make-a-function-to-find-duplicacy-in-a-character-string
	Aim: [
			'1. Here, original character means the character which '
				'is first time appearing in the string'
			'2. Replacing original character with => ('
			'3. If there are more occurences of original character'
				then replace them with => )'
	]
	References: http://www.pythonforbeginners.com/collection/python-collections-counter
"""
from collections import Counter

# Code
def duplicate_finder(word):
	word = word.lower()
	i = 1;

	for ch, count in Counter(word).items():
		# print '(', i, ') Original character: \'', ch, '\'with', count - 1, 'more occurence(s)'
		if count == 1:
			word = word.replace(ch, '(') # Only 1 occurence of original character	
		else:
			l = list(word)
			l[word.find(ch)] = '('       # Replace original character with (
			word = ''.join(l) 
			word = word.replace(ch, ')') # Replace other occurences of original character with )

		# print 1, 'occurence of \'', ch, '\' replaced with \'(\' and remaining ', count - 1, ' occurence(s) with \')\''
		# print 'Iteration ', i, ' gives: ', word, '\n'
		i += 1
	return word

# Test case 1
print "I/P:  abaccccsgfsyetgdggdh"
print "O/P: ", duplicate_finder('abaccccsgfsyetgdggdh')
"""
I/P:	abaccccsgfsyetgdggdh
O/P:	(()()))((()((()()))(
"""

# Test case 2
print "\nI/P:  AAABBBCCC34519543absd67das1729"
print "O/P: ", duplicate_finder('AAABBBCCC34519543absd67das1729')
"""
I/P:	AAABBBCCC34519543absd67das1729
O/p:	())())())((((()))))(((()))))()
"""
