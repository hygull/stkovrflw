// Input array
var arr = [
    {id:1,val: 5,name: 'Josh'},
    {id:2,val: 7,name: 'John'},
    {id:3,val: 6,name:'mike'},
    {id:4,val: 7,name: 'Andy'},
    {id:5,val: 8,name: 'Andrew'},
    {id:6,val: 7,name: 'Dave'}
]

// Empty array which we'll use to get our result and easily find the objects with similar values for 'val'
var obj = {};

arr.forEach((item) => {
    if (obj[item['val']] === undefined) {
        obj[item['val']] = item;
    } else {
        var id = obj[item['val']]['id'];
        var name = obj[item['val']]['name'];

        if(typeof id === 'number'){
            obj[item['val']]['id'] = [id, item['id']];
            obj[item['val']]['name'] = [name, item['name']];
        } else { // 'object'
            obj[item['val']]['id'].push(item['id']);
            obj[item['val']]['name'].push(item['name']);
        }
    }
})


var newArr = Object.values(obj);
// console.log(newArr);

// Pretty printing newArr
console.log(JSON.stringify(newArr, undefined, 4));

/*
    [
        {
            "id": 1,
            "val": 5,
            "name": "Josh"
        },
        {
            "id": 3,
            "val": 6,
            "name": "mike"
        },
        {
            "id": [
                2,
                4,
                6
            ],
            "val": 7,
            "name": [
                "John",
                "Andy",
                "Dave"
            ]
        },
        {
            "id": 5,
            "val": 8,
            "name": "Andrew"
        }
    ]
*/