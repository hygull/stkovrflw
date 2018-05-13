/**
	{
		"aim": Making an out of order array in order based on the element of another properly ordered array"
	}
*/

// const outOfOrderArray = [{field: 'rishi'}, {field: 'foo'}, {field: 'bar'}, {field: 'bazz'}, {field: 'bizz'}];
const outOfOrderArray = [{field: 'foo'}, {field: 'bar'}, {field: 'bazz'}, {field: 'bizz'}];

const arrayInProperOrder = [{field: 'bizz'}, {field: 'bazz'}, {field: 'foo'}, {field: 'bar'}];

// Printing out of order array
console.log("OUT OF ORDER ARRAY: \n", outOfOrderArray);

// Printing array in proper order
console.log("\nARRAY IN PROPER ORDER: \n", arrayInProperOrder);

var len = outOfOrderArray.length;
var removedItems = 0;

for (item of arrayInProperOrder) {
	console.log("Great")
	var index = outOfOrderArray.indexOf(item);
	console.log(item, index)
	if (index > -1) {
		removedItems += 1;
		outOfOrderArray.splice(index);
		outOfOrderArray.push(item);
	}
}

console.log(len);
console.log(removedItems)


console.log("\nUPDATED ARRAY (Which was out of order before): \n") 
console.log(outOfOrderArray);


