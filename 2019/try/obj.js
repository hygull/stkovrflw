// https://stackoverflow.com/questions/56015083/javascript-how-to-create-an-array-with-x-number-of-properties-from-another-ar/56015499#56015499
// Solved on 6 May 2019

function getNewArray(arr) {
	let newArr = [];

	if(arr.length) {
		let keys = ["0-1s", "1-2s"];
		
		newArr = keys.map((key) => {
			let newObj = {}
			console.log(newObj, key)

			for(let obj of arr) {				
				if(newObj["time"] === undefined) {
					newObj["time"] = key
				}
				newObj[obj["country"]] = obj[key]
			}

			return newObj
		})
	} 

	return newArr
}


function test() {
	let arr = [{
		   "0-1s": 6,
		   "1-2s": 2,
		   country: "us"
		}, {
		   "0-1s": 1,
		   "1-2s": 4,
		   country: "ja"
		}, {
		   "0-1s": 3,
		   "1-2s": 9,
		   country: "ca"
		}]

	let newArr = getNewArray(arr)
	console.log(newArr)
	/*
		[ { time: '0-1s', us: 6, ja: 1, ca: 3 },
	  { time: '1-2s', us: 2, ja: 4, ca: 9 } ]
	*/

	/* --- Pretty printing --- */
	console.log(JSON.stringify(newArr, null, 4))
	/*
		[
		    {
		        "time": "0-1s",
		        "us": 6,
		        "ja": 1,
		        "ca": 3
		    },
		    {
		        "time": "1-2s",
		        "us": 2,
		        "ja": 4,
		        "ca": 9
		    }
		]
	*/
}

//
test()