/*
	Function takes a string (data)
	Returns string with first 100 characters from index 0 to 100 (default)
	Returns string based on explicity passed values of start and end
*/
function get100charsNoCountBrsAndSpaces(data, start=0, end=100) {
	var arr = stringToArrWithNoBrsAndSpaces(data)
	let arrSpaces = arr.map((item) => {
		return item.join(' ')
	})

	let strBrsSpaces = arrSpaces.join(' '); // "sdd fhhf fhhhf fhhf"
	var finalStr;
	var spacesCount = 0;
	console.log("FinalMain: ", strBrsSpaces)
	i = 1
	do {
		console.log(i, '..................................')
		finalStr = strBrsSpaces.slice(start, end + spacesCount)
		console.log("Final string:", finalStr + "$$"+(finalStr.length))
		spacesCount = finalStr.match(/\s/gi).length
		console.log("Spaces", spacesCount)
		// end = end + spacesCount		
		console.log('OP: ', finalStr, end + spacesCount)
		i += 1
		// break
		console.log("Final len(test): ", finalStr.slice(start, end).split(' ').join('').length)
	} 
	while(finalStr.slice(start, end + spacesCount).split(' ').join('').length < 100);
	console.log("Returns............")
	return finalStr.slice(start, end + spacesCount)
}

/*
	Function that removes <br> and spaces from string (data) 
	and returns a 2d array (it helps us in recontruction of original string)
*/
function stringToArrWithNoBrsAndSpaces(data)  {
	var arrNoBrs = data.split('<br>')
	// console.log(JSON.stringify(arrNoBrs, null, 4))

	let arrNoBrsSpaces = arrNoBrs.map((item) => {
		let a = []; //let: local scope of a
		a = item.split(' ')
		return a;
	})

	// console.log(JSON.stringify(arrNoBrsSpaces, null, 4))
	return arrNoBrsSpaces
}

/*
	Function which reconstructs the string from the 2 array
	Adds spaces and <br> at proper places
*/
function arrWithNoBrsAndSpacesToString(array)  {
	let arrSpaces = array.map((item) => {
		return item.join(' ')
	})
	console.log(arrSpaces)
	// console.log(arrSpaces)
	let strBrsSpaces = arrSpaces.join('<br>')
	return strBrsSpaces
}

// ********* Testing: stringToArrsWithNoBrsAndSpaces()
var inputStr = `it to make a type specimen book. <br><br>It has survived not only five centuries, but also the leap into electronic typesetting, <br><br>remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages<br><br>, and more recently with desktop publishing software like Aldus PageMaker including&nbsp; versions of Lorem Ipsum.`
var arr = stringToArrWithNoBrsAndSpaces(inputStr)
console.log(arr)

console.log('\n')

// ********* Testing: arrWithNoBrsAndSpacesToString()
var str = arrWithNoBrsAndSpacesToString(arr)
console.log(str)

// ********* Testing: get100charsNoCountBrsAndSpaces(inputStr)
var finalData = get100charsNoCountBrsAndSpaces(inputStr)
console.log('Foffhhfh: ', finalData)
console.log('tynd66dhhs', finalData.length) // 160 (100 char + 60 spaces), see below line
console.log('46ghdd', finalData.split(' ').join('').length)

/* ...** Output: stringToArrsWithNoBrsAndSpaces(inputStr) **...

[
    [
        "it",
        "to",
        "make",
        "a",
        "type",
        "specimen",
        "book.",
        ""
    ],
    [
        ""
    ],
    [
        "It",
        "has",
        "survived",
        "not",
        "only",
        "five",
        "centuries,",
        "but",
        "also",
        "the",
        "leap",
        "into",
        "electronic",
        "typesetting,",
        ""
    ],
    [
        ""
    ],
    [
        "remaining",
        "essentially",
        "unchanged.",
        "It",
        "was",
        "popularised",
        "in",
        "the",
        "1960s",
        "with",
        "the",
        "release",
        "of",
        "Letraset",
        "sheets",
        "containing",
        "Lorem",
        "Ipsum",
        "passages"
    ],
    [
        ""
    ],
    [
        ",",
        "and",
        "more",
        "recently",
        "with",
        "desktop",
        "publishing",
        "software",
        "like",
        "Aldus",
        "PageMaker",
        "including&nbsp;",
        "versions",
        "of",
        "Lorem",
        "Ipsum."
    ]
]
*/


/* ...** Output: arrWithNoBrsAndSpacesToString(arr) **...

it to make a type specimen book. <br><br>It has survived not only five centuries, but also the leap into electronic typesetting, <br><br>remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages<br><br>, and more recently with desktop publishing software like Aldus PageMaker including&nbsp; versions of Lorem Ipsum.

*/


/* ...** Output: get100charsNoCountBrsAndSpaces(inputStr) **...


*/