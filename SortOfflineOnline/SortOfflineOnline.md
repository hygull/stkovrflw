**@Oj Obasi**, try the below code.

> It uses **map()** method defined on arrays.

    var objs = [ 
        { id: 'X82ns', name: 'james', presence: 'online' },
        { id: '8YSHJ',    name: 'mary', presence: 'offline' },
        { id: '7XHSK', name: 'rene', presence: 'online' }
    ];

    /* Pretty printing objs array*/
    console.log(JSON.stringify(objs, null, 4))  // Before modification (sorting)
    /*
    [
        {
            "id": "X82ns",
            "name": "james",
            "presence": "online"
        },
        {
            "id": "8YSHJ",
            "name": "mary",
            "presence": "offline"
        },
        {
            "id": "7XHSK",
            "name": "rene",
            "presence": "online"
        }
    ]
    */

    objs.map((item, index) => { 
    	if(item.presence === 'online') { // online, add to front then remove this item from its current position
    		objs.splice(0, 0, item) // add at front
    	} else { // offline, push at end then remove this item from its current position
    		objs.splice(objs.length, 1, item) // push at end	
    	}
    	objs.splice(index, 1) // remove
    })

    /* Pretty printing objs array */
    console.log(JSON.stringify(objs, null, 4))  // After modification (sorting)
    /*
    [
        {
            "id": "X82ns",
            "name": "james",
            "presence": "online"
        },
        {
            "id": "7XHSK",
            "name": "rene",
            "presence": "online"
        },
        {
            "id": "8YSHJ",
            "name": "mary",
            "presence": "offline"
        }
    ]
    */

