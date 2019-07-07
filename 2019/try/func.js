// function that creates new array with desired items and returns to the caller
function getAlteredArray(items, structure) {
	let newArr = items.map((obj, index) => {
		// obj => {"id":1,"title":"xxxxx","format":"horizontal","position":0}
		obj["format"] = structure[index]
		return obj
	})

	return newArr
}

// function that creates set of data needs to be passed to getAlteredArray() function
function test() {
	let items = [{"id":1,"title":"xxxxx","format":"horizontal","position":0}, 
            {"id":3,"title":"xxxxx","format":"vertical","position":1}, 
            {"id":6,"title":"xxxxx","format":"small","position":2}, 
            {"id":9,"title":"xxxxx","format":"small","position":3}, 
            {"id":11,"title":"xxxxx","format":"small","position":4}]

    // TEST 1 - Call getAlteredArray() with `items` & `structure`
    let structure = ["horizontal","vertical","vertical","vertical","small"]
    let newArr = getAlteredArray(items, structure)
    console.log(newArr)
    /*
		[ { id: 1, title: 'xxxxx', format: 'horizontal', position: 0 },
		  { id: 3, title: 'xxxxx', format: 'vertical', position: 1 },
		  { id: 6, title: 'xxxxx', format: 'vertical', position: 2 },
		  { id: 9, title: 'xxxxx', format: 'vertical', position: 3 },
		  { id: 11, title: 'xxxxx', format: 'small', position: 4 } ]
	*/

    // TEST 2 
	let structure2 = ["horizontal","vertical","small","small","small"]
    let newArr2 = getAlteredArray(items, structure2)
    console.log(newArr2)
    /*
		[ { id: 1, title: 'xxxxx', format: 'horizontal', position: 0 },
		  { id: 3, title: 'xxxxx', format: 'vertical', position: 1 },
		  { id: 6, title: 'xxxxx', format: 'small', position: 2 },
		  { id: 9, title: 'xxxxx', format: 'small', position: 3 },
		  { id: 11, title: 'xxxxx', format: 'small', position: 4 } ]	
	*/
}

// Start
test()