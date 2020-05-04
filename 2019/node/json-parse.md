Just to understand where exactly you have to do the modification and what little mistake you did has already been pointed out in the above comments. 

	> var arr = [ "{\"id\": \"amzn\", \"price\": 1785.6600341796875, \"_attachments\": \"attachments/\"}", "{\"id\": \"msft\", \"price\": 138.42999267578125, \"_attachments\": \"attachments/\"}", "{\"id\": \"googl\", \"price\": 1244.280029296875, \"_attachments\": \"attachments/\"}", "{\"id\": \"ba\", \"price\": 331.05999755859375, \"_attachments\": \"attachments/\"}", "{\"id\": \"air.pa\", \"price\": 122, \"_attachments\": \"attachments/\"}" ]
	undefined
	> 
	> item0 = arr[0]
	'{"id": "amzn", "price": 1785.6600341796875, "_attachments": "attachments/"}'
	> 
	> item0Obj = JSON.parse(item0)
	{ id: 'amzn', price: 1785.6600341796875, _attachments: 'attachments/' }
	> 
	> item0Obj.id
	'amzn'
	> item0Obj.price
	1785.6600341796875
	> item0Obj._attachments
	'attachments/'
	> 

And finally, let's do it for all.


	> // Do it for all
	undefined
	> newArr = arr.map((str) => JSON.parse(str))
	[
	  {
	    id: 'amzn',
	    price: 1785.6600341796875,
	    _attachments: 'attachments/'
	  },
	  {
	    id: 'msft',
	    price: 138.42999267578125,
	    _attachments: 'attachments/'
	  },
	  {
	    id: 'googl',
	    price: 1244.280029296875,
	    _attachments: 'attachments/'
	  },
	  { id: 'ba', price: 331.05999755859375, _attachments: 'attachments/' },
	  { id: 'air.pa', price: 122, _attachments: 'attachments/' }
	]
	> 

After that you will have an access to inner elements of array.

	> // List out all prices
	undefined
	> for(let obj of newArr) {
	... console.log(obj.price) // obj["price"] can also be used here
	... }
	1785.6600341796875
	138.42999267578125
	1244.280029296875
	331.05999755859375
	122
	undefined
	> 
	> for(let obj of newArr) {
	... console.log(obj["price"]) // obj.price can also be used here
	... }
	1785.6600341796875
	138.42999267578125
	1244.280029296875
	331.05999755859375
	122
	undefined
	> 

So just check the `response.data` and its type using `console.log(response.data, typeof response.data)` and take below decisions.

If

+ `response.data` is  something like `["{\"k\": \"v\"}", "\"k2\": \"v2\""]` as you are printing then you have to use `app.stocks = response.data.map((obj) => JSON.parse(obj))`.
+ `response.data` is something like `[{"k": "v"}, {"k2": "v2"}]` then you just need to use `app.stocks = response.data` (as it's already a list of objects).
+ response.data is something like `'[{"k": "v"}, "k2": "v2"]'` (string) as you are printing then you have to use `app.stocks = JSON.parse(response.data)`.

Take your decisions properly and think about your `response.data`, its type may be `'object'` | `'string'`. And use `JSON.parse()` to get object form, if any of your list item is in string form. 