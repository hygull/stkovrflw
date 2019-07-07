
function timeToGetNumberLessThan10(num) {
	var s = '' + num
	var chars = []

	if(s.length == 1)
		return 1

	sum = 1

	for(var i=0; i < s.length; i++) {
		chars.push(s[i])
		sum *= parseInt(s[i])
	}

	// Log message
	console.log(chars.join(' * ') + ' = ' + sum) 

	if(sum < 10) {
		return 1
	} else {
		// Recursive call
		return 1 + timeToGetNumberLessThan10(sum)
	}
}


// TEST 1
var count = timeToGetNumberLessThan10(39);
console.log('============')
console.log(count + ' times')

console.log('\n') // New line

// TEST 2
var count = timeToGetNumberLessThan10(786);
console.log('============')
console.log(count + ' times')

/*
3 * 9 = 27
2 * 7 = 14
1 * 4 = 4
============
3 times


7 * 8 * 6 = 336
3 * 3 * 6 = 54
5 * 4 = 20
2 * 0 = 0
============
4 times
*/
