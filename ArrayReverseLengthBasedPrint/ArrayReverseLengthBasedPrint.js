var arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

// $('button').click(function() {
// var index = $('#index').val();
// var index = parseInt($('#index').val());
var index = 9;

// var length = $('#length').val();
// var length = parseInt($('#length').val());
var length = 2;
var newItems = []
index = index - 1
// for (var i = arr.length; i > (arr.length - length); i--) {
for (var i = index; (i > -1) && (i > index-length); i--) {
	console.log(i)
	newItems.push(arr[i])
}

console.log(newItems)
// })