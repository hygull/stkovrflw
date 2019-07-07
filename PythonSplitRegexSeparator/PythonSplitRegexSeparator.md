**@Duy**, have a look at the following 2 examples.

> I've used the concept of **list comprehension** & string's **split()** method.

	### Example 1
	>>> string = 'Hello, happy [4th of July]. I love the [[firework]]'
	>>>
	>>> part1 = string.split('[')
	>>> part1
	['Hello, happy ', '4th of July]. I love the ', '', 'firework]]']
	>>>
	>>> part2 = [s[:s.index(']')] for s in part1 if ']' in s and not ']]' in s]
	>>> part2
	['4th of July']
	>>>

### Example 2

	>>> sentence1 = "This is [Great opportunity] to [[learn]] [Nice things] and [Programming] [[One]] of them]."
	>>> part1 = sentence1.split('[')
	>>> part2 = [s[:s.index(']')] for s in part1 if ']' in s and not ']]' in s]
	>>> part2
	['Great opportunity', 'Nice things', 'Programming']
	>>>

The below code is your 2nd input text.

### Example 3

	>>> import re
	>>>
	>>> string2 = "text = {{Hey, how are you.}} I've watched John Mulaney all night. [[Category: Comedy]] [[Image: John Mulaney]]"
	>>>
	>>> part1 = re.split('[\{\[]', string2)
	>>> part1
	['text = ', '', "Hey, how are you.}} I've watched John Mulaney all night. ", '', 'Category: Comedy]] ', '', 'Image: John Mulaney]]']
	>>> part3 = [ "[["+ s[:s.index(']]') + 2] if ']]' in s else "{{" + s[:s.index('}}') + 2]  for s in part1 if ']]' in s or '}}' in s]
	>>>
	>>> part3
	['{{Hey, how are you.}}', '[[Category: Comedy]]', '[[Image: John Mulaney]]']
	>>>