# stkovrflw
A project containing the code examples related to different kind of questions and their detailed solutions (that I solved on Stackoverflow). 

### 1

> [https://stackoverflow.com/questions/56015083/javascr...](https://stackoverflow.com/questions/56015083/javascript-how-to-create-an-array-with-x-number-of-properties-from-another-ar/56015499#56015499)

```javascript
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
```

### 2

> [https://stackoverflow.com/questions/56095946/how-do-i-convert-a-map-object-to-list-and-also-assign-to-a-variable/56096030#56096030](https://stackoverflow.com/questions/56095946/how-do-i-convert-a-map-object-to-list-and-also-assign-to-a-variable/56096030#56096030)

Once you will 

+ learn/know about how Python generator works

+ write/create your own generators

you will easily figure out this problem (looks strange but very useful and simple).

> Thanks to **yield** keyword & **StopIteration** exception & some magic methods as these play great roles in writing our own generator.

```python
Python 3.6.7 (v3.6.7:6ec5cf24b7, Oct 20 2018, 03:02:14) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> arr = [1729, 67, 92]
>>> gen = map(str, arr)
>>> 
>>> # 1st item
... 
>>> gen.__next__()
'1729'
>>> 
>>> # 2nd item
... 
>>> gen.__next__()
'67'
>>> 
>>> # 3rd item
... 
>>> gen.__next__()
'92'
>>> 
>>> # This will not work (Exception beacause no more items are in generator, over)
... 
>>> gen.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> 
```

So if you will focus on below kind of examples, you will be confused (1st time).

```python
>>> arr2 = list(gen)
>>> arr2
['1729', '67', '92']
>>>
>>> # Generator has already been iterated, so no more items
...
>>> gen.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>>
>>> arr2 = list(gen)
>>> arr2
[]
>>> 
```

Just for references, have a look at below links.

+ https://www.programiz.com/python-programming/generator

+ https://dbader.org/blog/python-generator-expressions