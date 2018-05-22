var data = `it to make a type specimen book. <br><br>It has survived not only five centuries, but also the leap into electronic typesetting, <br><br>remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages<br><br>, and more recently with desktop publishing software like Aldus PageMaker including&nbsp; versions of Lorem Ipsum.`
// removes nbsp
// var docDesc = data.replace(/[&]nbsp[;]/gi," "); 
// removes br
// var stringData = docDesc.replace(/[<]br[^>]*[>]/gi,""); 
var arrNoBrs = data.split('<br>')
console.log(JSON.stringify(arrNoBrs, null, 4))

var arrNoNbsps = arrNoBrs.map((item) => {
	var a = []
	a = item.split(' ')
	return a;
})

console.log(JSON.stringify(arrNoNbsps, null, 4))

// var stringData = arr.join('')
// var subData =  stringData.substr(0,100)
// function test(subData) {
    
// 	var n = subData.split(" ");
    
// 	return n.slice(Math.max(n.length - 5, 1))


// }

// var lastData = test(subData);
// var lastString = lastData.join(" ")
// var finalData = data.substring(0,data.indexOf(lastString)) + lastString

// var finalData = arrNoNbsps.join('')
// console.log(finalData)
// console.log(finalData.length)