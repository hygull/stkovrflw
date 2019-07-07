**@CyberJunkie**, You can fix it by using the concept of **Object destruction** as follows.

> **Note**: Visit [Destructuring assignment](https://javascript.info/destructuring-assignment) and [Destructuring assignment - Mozilla.org's documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment) to read about **Destructing objects**.



Thanks.

function getObj(attributes)
{
	const { one: newOne = '', two: newTwo = '', three: newThree = '' } = attributes;

	// var oneValue = one ? one : "";
	// var twoValue = two ? two : "";
	// var threeValue = three ? three : "";
	var props = {four: "The four", six: "The six"};

	return Object.assign( props, { 
	  "data-one": newOne,
	  "data-two": newTwo,
	  "data-three": newThree  
	} );
}

var prettyObj = JSON.stringify(getObj({one: "ObjData1.1", two: 'ObjData2', three: 'ObjData3'}), null, 4);
console.log(prettyObj)
/*
	{
	    "four": "The four",
	    "six": "The six",
	    "data-one": "ObjData1.1",
	    "data-two": "ObjData2",
	    "data-three": "ObjData3"
	}
*/

prettyObj = JSON.stringify(getObj({one: "ObjData1.2", two: 'ObjData2'}), null, 4);
console.log(prettyObj)
/*
	{
	    "four": "The four",
	    "six": "The six",
	    "data-one": "ObjData1.2",
	    "data-two": "ObjData2",
	    "data-three": ""
	}
*/

prettyObj = JSON.stringify(getObj({one: "ObjData1.2"}), null, 4)
console.log(prettyObj)
/*
	{
	    "four": "The four",
	    "six": "The six",
	    "data-one": "ObjData1.2",
	    "data-two": "",
	    "data-three": ""
	}
*/



	H:\RishikeshAgrawani\Projects\Stk\UndefinedValue>node
	>
	> // Example 1
	undefined
	>
	> attributes = {one: "ObjData1.2", two: 'ObjData2'}
	{ one: 'ObjData1.2', two: 'ObjData2' }
	>
	> const { one: newOne = '', two: newTwo = '', three: newThree = '' } = attributes;
	undefined
	>
	> one
	ReferenceError: one is not defined
	>
	> newOne
	'ObjData1.2'
	>
	> newTwo
	'ObjData2'
	>
	> newThree
	''
	>
	> // Example 2
	undefined
	> attributes2 = {one: "ObjData1.2", two: 'ObjData2'}
	{ one: 'ObjData1.2', two: 'ObjData2' }
	>
	> const { one = '', two ='', three = '' } = attributes;
	undefined
	> one
	'ObjData1.2'
	> two
	'ObjData2'
	> three
	''
	>


as it presents the difference between `const { one: newOne = '', two: newTwo = '', three: newThree = '' } = attributes;` and `attributes2 = {one: "ObjData1.2", two: 'ObjData2'}` statements.