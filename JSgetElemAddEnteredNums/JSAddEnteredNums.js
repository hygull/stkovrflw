var productPrice = document.getElementById("productPrice");

var totalPrice = document.getElementById("totalPrice");

var addAlert = document.getElementById("addAlert");

var arr = [];

function addToCart() { // onclick Event to add and show the price
 	arr.push(productPrice.innerHTML);
	
	function getSum(total, num) {
	 return total + num;
	}

	var tempTotal = arr.reduce(getSum);
	totalPrice.innerHTML = tempTotal;
}