**@Marcel**, as you are satisfied with the above approach suggested by **@Kasramvd**, it is good and  I want to suggest you to write a simple tiny function using `lambda` keyword. Call it multiple times with new parameters and get the output as the below code shows.

> Visit and check https://www.python-course.eu/lambda.php for detailed examples.
>
> See [Python lambda function](http://thepythonguru.com/python-lambda-function/) for brief knowledge.

	>>> get_string = lambda s: s.split(';')[0] + s.split(';')[-1]
	>>>
	>>> get_string("abcd;efghij;klmn")
	'abcdklmn'
	>>>
	>>> get_string("ABCD;MONKEY;XYZ")
	'ABCDXYZ'
	>>>
	>>> get_string("PYTHON;abcd;LEARN")
	'PYTHONLEARN'
	>>>