**@Tanjore**, better is that you try to organize your ids inside an object as follows.

> All the ids with value `5` which is `1` here so `{'5': [1]}`.
>
> All the ids with value `6` which is `3` here so `{'3': [3]}`.
>
> All the ids with value `7` which are `2, 3, 4` here so `{'7': [2, 3, 4]}`.
>
> ...
>

We can have an object similar to this.

    {
        "5": [
            1
        ],
        "6": [
            3
        ],
        "7": [
            2,
            4,
            6
        ],
        "8": [
            5
        ]
    }


Let's create the above object on **Node REPL**.

    > var arr = [
    ...   {id:1,val: 5,name: 'Josh'},
    ...   {id:2,val: 7,name: 'John'},
    ...   {id:3,val: 6,name:'mike'},
    ...   {id:4,val: 7,name: 'Andy'},
    ...   {id:5,val: 8,name: 'Andrew'},
    ...   {id:6,val: 7,name: 'Dave'}
    ... ]
    undefined
    >
    > var obj = {}
    undefined
    >
    > arr.forEach((item) => {
    ... if (obj[item['val']] === undefined) {
    ..... obj[item['val']] = [item['id']];
    ..... } else {
    ..... obj[item['val']].push(item['id']);
    ..... }
    ... })
    undefined
    >
    > obj
    { '5': [ 1 ], '6': [ 3 ], '7': [ 2, 4, 6 ], '8': [ 5 ] }
    >
    > JSON.stringify(obj, undefined, 4)
    '{\n    "5": [\n        1\n    ],\n    "6": [\n        3\n    ],\n    "7": [\n        2,\n        4,\n        6\n    ],\n    "8": [\n        5\n    ]\n}'
    >
    > console.log(JSON.stringify(obj, undefined, 4))
    {
        "5": [
            1
        ],
        "6": [
            3
        ],
        "7": [
            2,
            4,
            6
        ],
        "8": [
            5
        ]
    }
    undefined
    >

Finally, you can obtain the below array which you want based on the above concept.

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

Check the below code which gives you an array you want.

