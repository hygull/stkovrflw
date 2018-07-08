var someArray = ["5 5", "5 6", "5 12", "4 12"];

var obj = {}

for(var i=0; i<someArray.length; i++) {
	numbers = someArray[i].split(/\s+/)  // regular expression technique for multiple spaces
	
	if(obj[numbers[0]] === undefined)
		obj[numbers[0]] = [numbers[1]]
	else
		obj[numbers[0]].push(numbers[1])
}

console.log(JSON.stringify(obj, null, 4))

/*
{
    "4": [
        "12"
    ],
    "5": [
        "5",
        "6",
        "12"
    ]
}
*/

// console.log(obj['4'])
// // [ '12' ]

// console.log(obj['5'])
// // [ '5', '6', '12' ]