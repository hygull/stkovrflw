**@Tankit88**, you will need to convert string formed numbers in array to number i.e. `'2000' => 2000` using `parseInt()` which is clear in the executed code on **Node REPL** after the below code.

	var productPrice = document.getElementById("productPrice");
	var totalPrice = document.getElementById("totalPrice");
	var addAlert = document.getElementById("addAlert");

	var arr = [];

	function addToCart() { // onclick Event to add and show the price
		arr.push(parseInt(productPrice.innerHTML));
		
		function getSum(total, num) {
			return total + num;
		}

		var tempTotal = arr.reduce(getSum);
		totalPrice.innerHTML = tempTotal;
	}

Finally, have a look at the below executed lines on **Node REPL** which clarifies the above code's logic.

	> arr = ['2000', '2000', '2000']
	[ '2000', '2000', '2000' ]
	>
	> function getSum(total, num) {
	...  return total + num;
	... }
	undefined
	>
	> var tempTotal = arr.reduce(getSum);
	undefined
	>
	> tempTotal
	'200020002000'
	>
	> // A little change to solve above problem
	undefined
	> function getSum(total, num) {
	...  return parseInt(total) + parseInt(num);
	... }
	undefined
	>
	> var tempTotal = arr.reduce(getSum);
	undefined
	>
	> tempTotal
	6000
	>

Thanks.