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