**@Mark**, here I've shown 3 ways to solve the problem. Please check it and let me know if it satisfies your problem or not with some set of new inputs and expected outputs.
I'll update the code based on that.

### First way - Using list comprehension, extend(), set()

> try it online at http://rextester.com/WEE27295.

    # List of strings
    my_list = ['john', 'james', 'joey']

    # List of dictionaries
    results = [{"name": 'john', "age": 20}, {"name": 'james', "age": 25}]

    new_persons = [{"name": name, "age": 30} for name in set(my_list) if name not in set((person["name"] for person in results))];
    results.extend(new_persons);

    print(results)

&raquo; Output

    [{'age': 20, 'name': 'john'}, {'age': 25, 'name': 'james'}, {'age': 30, 'name': 'joey'}]   

### &raquo; Second way - Using set()

> Try it online at http://rextester.com/WBAT64136.

	# List of strings
	my_list = ['john', 'james', 'joey']

	# List of dictionaries
	results = [{"name": 'john', "age": 20}, {"name": 'james', "age": 25}]
	unique_names = set((person["name"] for person in results));

	for name in my_list:
	   if name not in unique_names:
	       new_person = {
	           'name': name,
	           'age': 30
	       }
	       results.append(new_person);
	                
	print(results)

&&raquo; Output

    [{'age': 20, 'name': 'john'}, {'age': 25, 'name': 'james'}, {'age': 30, 'name': 'joey'}]

### &raquo; Third way - Using nested loops

> Try it online at http://rextester.com/DSB44497.

    # List of strings
    my_list = ['john', 'james', 'joey']

    # List of dictionaries
    results = [{"name": 'john', "age": 20}, {"name": 'james', "age": 25}]

    for name in my_list:
     found = False;
     for person in results:
         if person["name"] == name:
              found = True

     if not found:
         new_person = {
             'name': name,
             'age': 30
         }
         results.append(new_person);
                  
    print(results)


&raquo; Output

    [{'name': 'john', 'age': 20}, {'name': 'james', 'age': 25}, {'name': 'joey', 'age': 30}]

