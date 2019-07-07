**@Angel**, you are trying to compare a list i.e. `keywords` to a string `userString` which is wrong.

You just have to check for the existence of string inside list as follows.

	>>> import keyword
	>>> kwords_list = keyword.kwlist
	>>>
	>>> kwords_list
	['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
	>>>
	>>> for i in range(1, 5):
	...     word = raw_input('Enter any word: ');
	...     if word.strip() in kwords_list:
	...         print(word.strip(), 'is a keyword')
	...     else:
	...         print(word.strip(), 'is not a keyword')
	...
	Enter any word: if
	('if', 'is a keyword')
	Enter any word: else
	('else', 'is a keyword')
	Enter any word: lambda
	('lambda', 'is a keyword')
	Enter any word: for
	('for', 'is a keyword')
	>>>