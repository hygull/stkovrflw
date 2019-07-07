var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

$('button').click(function() {
	// var index = $('#index').val();
	var index = parseInt($('#index').val()); // ADDED (CONVERTING TO INTEGER)

	// var length = $('#length').val();
	var length = parseInt($('#length').val()); // ADDED (CONVERTING TO INTEGER)

	var newItems = []
	index = index - 1; // ADDED
	// for (var i = arr.length; i > (arr.length - length); i--) {
	for (var i = index; (i > -1) && (i > index-length); i--) { // ADDED
		// console.log(i)
		newItems.push(arr[i])
	}

	console.log(newItems)
})