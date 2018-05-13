/**
	{
		"aim": Making an out of order array in order based on the element of another properly ordered array"
	}
*/

function f(outOfOrderArray, arrayInProperOrder) {
	// Printing out of order array
	console.log("OUT OF ORDER ARRAY: \n", outOfOrderArray);

	// Printing array in proper order
	console.log("\nARRAY IN PROPER ORDER: \n", arrayInProperOrder);

	var len = arrayInProperOrder.length;
	var removedItems = 0;

	for (item of arrayInProperOrder) {
		var index = outOfOrderArray.indexOf(item);

		if (index > -1) {
			removedItems += 1;
			outOfOrderArray.splice(index);
			outOfOrderArray.push(item);
		}
	}


	console.log("\nUPDATED ARRAY (Which was out of order before: \n") 
	console.log(outOfOrderArray);
}

const outOfOrderArray = [{field: 'foo'}, {field: 'bar'}, {field: 'bazz'}, {field: 'bizz'}];

const arrayInProperOrder = [{field: 'bizz'}, {field: 'bazz'}, {field: 'foo'}, {field: 'bar'}];