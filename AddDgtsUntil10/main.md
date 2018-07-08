# https://stackoverflow.com/questions/51230823/using-a-while-loop-to-split-an-integer-into-digits-then-multiply-digits-togethe/51231073#51231073

**@daggett**, if you prefer to use **recursion** then following code will also work for your problem but I do not recommend you to use this. I just presented to solve your problem using recursion which is a great concepts used in large applications to simply the tasks.

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
