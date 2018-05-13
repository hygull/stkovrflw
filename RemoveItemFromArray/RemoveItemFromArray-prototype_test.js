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

