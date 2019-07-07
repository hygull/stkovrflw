Define a method name remove() on array objects using prototying feature of JavaScript.

> Use **splice()** method to fulfill your requirement.

Please have a look at the below code.

	Array.prototype.remove = function(item) {
		// index will have -1 if item does not exist
		// else it will have the index of 1st item found in array
		var index = this.indexOf(item); 
		
		if (index > -1) {
			// splice() method is used to add/remove items(s) in array
			this.splice(index, 1); 
		}

		return index;
	}


	var arr = [ 11, 22, 67, 45, 61, 89, 34, 12, 7, 8, 3, -1, -4];

	// Printing array
	// [ 11, 22, 67, 45, 61, 89, 34, 12, 7, 8, 3, -1, -4];
	console.log(arr)

	// Removing 67 (getting its index i.e. 2)
	console.log("Removing 67")
	var index = arr.remove(67)

	if (index > 0){
		console.log("Item 67 found at ", index)
	} else {
		console.log("Item 67 does not exist in array")
	}

	// Printing updated array
	// [ 11, 22, 45, 61, 89, 34, 12, 7, 8, 3, -1, -4];
	console.log(arr)

	// ............... Output ................................
	// [ 11, 22, 67, 45, 61, 89, 34, 12, 7, 8, 3, -1, -4 ]
	// Removing 67
	// Item 67 found at  2
	// [ 11, 22, 45, 61, 89, 34, 12, 7, 8, 3, -1, -4 ]

> **Note:** Below is the full example code executed on **Node.js REPL** which describes the use of push(), pop(), shift(), unshift() and splice() methods.

	> // Defining an array
	undefined
	> var arr = [12, 45, 67, 89, 34, 12, 7, 8, 3, -1, -4, -11, 0, 56, 12, 34];
	undefined
	> // Getting length of array
	undefined
	> arr.length;
	16
	> // Adding 1 more item at the end i.e. pushing an item
	undefined
	> arr.push(55);
	17
	> arr
	[ 12, 45, 67, 89, 34, 12, 7, 8, 3, -1, -4, -11, 0, 56, 12, 34, 55 ]
	> // Popping item from array (i.e. from end)
	undefined
	> arr.pop()
	55
	> arr
	[ 12, 45, 67, 89, 34, 12, 7, 8, 3, -1, -4, -11, 0, 56, 12, 34 ]
	> // Remove item from beginning
	undefined
	> arr.shift()
	12
	> arr
	[ 45, 67, 89, 34, 12, 7, 8, 3, -1, -4, -11, 0, 56, 12, 34 ]
	> // Add item(s) at beginning
	undefined
	> arr.unshift(67); // Add 67 at begining of the array and return number of items in updated/new array
	16
	> arr
	[ 67, 45, 67, 89, 34, 12, 7, 8, 3, -1, -4, -11, 0, 56, 12, 34 ]
	> arr.unshift(11, 22); // Adding 2 more items at the beginning of array
	18
	> arr
	[ 11, 22, 67, 45, 67, 89, 34, 12, 7, 8, 3, -1, -4, -11, 0, 56, 12, 34 ]
	>
	> // Define a method on array (temorarily) to remove an item and return the index of removed item; if it is found else return -1
	undefined
	> Array.prototype.remove = function(item) {
	... var index = this.indexOf(item);
	... if (index > -1) {
	..... this.splice(index, 1); // splice() method is used to add/remove items in array
	..... }
	... return index;
	... }
	[Function]
	>
	> arr
	[ 11, 22, 67, 45, 67, 89, 34, 12, 7, 8, 3, -1, -4, -11, 0, 56, 12, 34 ]
	>
	> arr.remove(45);	// Remove 45 (You will get the index of removed item)
	3
	> arr
	[ 11, 22, 67, 67, 89, 34, 12, 7, 8, 3, -1, -4, -11, 0, 56, 12, 34 ]
	>
	> arr.remove(22)	// Remove 22
	1
	> arr
	[ 11, 67, 67, 89, 34, 12, 7, 8, 3, -1, -4, -11, 0, 56, 12, 34 ]
	> arr.remove(67)	// Remove 67
	1
	> arr
	[ 11, 67, 89, 34, 12, 7, 8, 3, -1, -4, -11, 0, 56, 12, 34 ]
	>
	> arr.remove(89)	// Remove 89
	2
	> arr
	[ 11, 67, 34, 12, 7, 8, 3, -1, -4, -11, 0, 56, 12, 34 ]
	>
	> arr.remove(100);  // 100 doesn't exist, remove() will return -1
	-1
	>

Thanks.