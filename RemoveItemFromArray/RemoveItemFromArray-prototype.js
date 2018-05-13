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
