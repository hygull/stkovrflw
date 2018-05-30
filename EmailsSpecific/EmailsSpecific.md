**@Danny**, you can also get the expected output with just 1 line of code using Python's **list comprehension**, **map()**, **filter()**, **lambda function** etc. as the below code examples shows. 

> Check [Lambda, filter(), map()](https://www.python-course.eu/lambda.php) and [List comprehension](https://www.python-course.eu/list_comprehension.php). It's really good to use these concepts in programming.

## 1 line code

	emails_new = list(filter(lambda email_all_dict: True if sum(list(map(lambda email_exist_dict: True if email_exist_dict["email"] == email_all_dict['email'] else False, emails_exist))) == 0 else False, emails_all))

## Example 1

	emails_all = [{'email': 'new@email.com', 'first_name': 'New Name'}, {'email': 'exists@email.com', 'first_name': 'Exists Name'}]

	emails_exist = [{'email': 'exists@email.com'}]

	emails_new = list(filter(lambda email_all_dict: True if sum(list(map(lambda email_exist_dict: True if email_exist_dict["email"] == email_all_dict['email'] else False, emails_exist))) == 0 else False, emails_all))

	print(emails_new)

	# [{'first_name': 'New Name', 'email': 'new@email.com'}]


## Example 2

	emails_all = [
			{'email': 'new1@email.com', 'first_name': 'New Name1'}, 
			{'email': 'exists1@email.com', 'first_name': 'Exists Name1'},
			{'email': 'exists2@email.com', 'first_name': 'Exists Name2'},
			{'email': 'exists5@email.com', 'first_name': 'Exists Name5'},
			{'email': 'exists6@email.com', 'first_name': 'Exists Name6'},
			{'email': 'new9@email.com', 'first_name': 'New Name9'}, 
			{'email': 'exists7@email.com', 'first_name': 'Exists Name7'},
			{'email': 'exists8@email.com', 'first_name': 'Exists Name8'},
			{'email': 'exists4@email.com', 'first_name': 'Exists Name4'},
			{'email': 'new4@email.com', 'first_name': 'New Name4'}, 
			{'email': 'new2@email.com', 'first_name': 'New Name2'}, 
			{'email': 'exists3@email.com', 'first_name': 'Exists Name3'}
	]

	emails_exist = [
			{'email': 'exists@email.com'},    # Does not exist
			{'email': 'exists7@email.com', 'first_name': 'Exists Name7'},
			{'email': 'exists8@email.com', 'first_name': 'Exists Name8'},
			{'email': 'exists4@email.com', 'first_name': 'Exists Name4'}
	]

	emails_new2 = list(filter(lambda email_all_dict: True if sum(list(map(lambda email_exist_dict: True if email_exist_dict["email"] == email_all_dict['email'] else False, emails_exist))) == 0 else False, emails_all))

	# Pretty printing list
	print(json.dumps(emails_new2, indent=4))

	"""
	[
	    {
	        "first_name": "New Name1",
	        "email": "new1@email.com"
	    },
	    {
	        "first_name": "Exists Name1",
	        "email": "exists1@email.com"
	    },
	    {
	        "first_name": "Exists Name2",
	        "email": "exists2@email.com"
	    },
	    {
	        "first_name": "Exists Name5",
	        "email": "exists5@email.com"
	    },
	    {
	        "first_name": "Exists Name6",
	        "email": "exists6@email.com"
	    },
	    {
	        "first_name": "New Name9",
	        "email": "new9@email.com"
	    },
	    {
	        "first_name": "New Name4",
	        "email": "new4@email.com"
	    },
	    {
	        "first_name": "New Name2",
	        "email": "new2@email.com"
	    },
	    {
	        "first_name": "Exists Name3",
	        "email": "exists3@email.com"
	    }
	]
	"""