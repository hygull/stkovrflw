Please have a look at the below test code. 

You can easily understand it. Finally, I have used your provided code after this. The code focuses on concatenation of variables and strings.

	> var a = 67
	undefined
	> var name = 'JavaScript'
	undefined
	>
	> a + ""
	'67'
	> a + name
	'67JavaScript'
	> "'" + name + "'"
	'\'JavaScript\''
	>
	> '"' + name + '"'
	'"JavaScript"'
	>
	> var obj = '{ "name": "Rishikesh", "age": 26}'
	undefined
	> obj
	'{ "name": "Rishikesh", "age": 26}'
	>
	> typeof obj
	'string'
	>
	> // Coversion in real JS object
	undefined
	> realObj = JSON.parse(obj);
	{ name: 'Rishikesh', age: 26 }
	>
	> realObj.name
	'Rishikesh'
	>
	> realObj.age
	26
	>

There are other methods too. You can comment for more help.

> **Note:** Make sure, you have properly used quotes &raquo; `'` and `"`.

	// A sample test code 
	var arr = [67]; // Array of 1 item

	var MYVARIABLE1 = 'Wednesday'
	var MYVARIABLE2 = '01:05'
	var MYVARIABLE3 = '02:06'
	var data2 = null;

	for (var i=0; i < arr.length; ++i){
	    data2 = '[{' +
	    		'"day": "' + MYVARIABLE1 + '",' + 
	    		'"periods":[{' +
	    				'"start":"' + MYVARIABLE2 + '",' +
	    				'"end":"' + MYVARIABLE3 + '"' +
	    				'}]' + 
	    	  '}]';
	}

	console.log(data2)
	// [{"day": "Wednesday","periods":[{"start":"01:05","end":"02:06"}]}]

