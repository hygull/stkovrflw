// https://stackoverflow.com/questions/50434025/add-a-top-list-in-each-object-of-my-array

var newObj = {}
var colors = []


var myArray =  [
    {Color:"red", Fruit:"apple", Country:"us", Value:1},
    {Color:"red", Fruit:"cherry", Country:"us", Value:1},
    {Color:"red", Fruit:"apple", Country:"italy", Value:1},
    {Color:"red", Fruit:"apple", Country:"italy", Value:2}, 
    {Color:"red", Fruit:"strawberry", Country:"italy", Value:2},                
    {Color:"red", Fruit:"cherry", Country:"italy", Value:1},
    {Color:"yellow", Fruit:"banana", Country:"us", Value:1},
    {Color:"yellow", Fruit:"banana", Country:"italy", Value:1},
    {Color:"yellow", Fruit:"pineapple", Country:"italy", Value:5},
    {Color:"yellow", Fruit:"mango", Country:"italy", Value:1},          
];

/*
    {
        red: {
            'fruits': [
                {},
                {}
            ],
            values: [
                7,
                9,
            ]
        },
        yellow: {
            'fruits': [
                {},
                {}
            ],
            values: [
                11,
                12
            ]
        }
    }
*/
for(let obj of myArray) {
        var color = obj.Color;

        // Add color as key of obj that points list of objects of same color
        if(newObj[color] === undefined) {
            // Create new
            newObj[color] = {}
            newObj[color].fruits = []
            colors.push(color)
            // console.log('Created')
            // console.log(newObj)
            newObj[color]['fruits'].push(obj)
            newObj[color]['values'] = [obj.Value]
            // console.log(newObj)
            // console.log(newObj[color]['fruits']['Country'])
        } else {
            // Push fruit
            newObj[color].fruits.push(obj);

            // Checking values (Creating a list of unique values)
            if(newObj[color]['values'].indexOf(obj.Value) < 0) {
                newObj[color]['values'].push(obj.Value)
            }
        }
}

// Printing array of unique colors
console.log(colors);
/*
    [ 'red', 'yellow' ]
*/

// Sort colors array 
colors = colors.sort()
console.log("Sorted colors array: ", colors)

// Pretty printing object
console.log(JSON.stringify(newObj, null, 4));

/*
{
    "red": {
        "fruits": [
            {
                "Color": "red",
                "Fruit": "apple",
                "Country": "us",
                "Value": 1
            },
            {
                "Color": "red",
                "Fruit": "cherry",
                "Country": "us",
                "Value": 1
            },
            {
                "Color": "red",
                "Fruit": "apple",
                "Country": "italy",
                "Value": 1
            },
            {
                "Color": "red",
                "Fruit": "apple",
                "Country": "italy",
                "Value": 2
            },
            {
                "Color": "red",
                "Fruit": "strawberry",
                "Country": "italy",
                "Value": 2
            },
            {
                "Color": "red",
                "Fruit": "cherry",
                "Country": "italy",
                "Value": 1
            }
        ],
        "values": [
            1,
            2
        ]
    },
    "yellow": {
        "fruits": [
            {
                "Color": "yellow",
                "Fruit": "banana",
                "Country": "us",
                "Value": 1
            },
            {
                "Color": "yellow",
                "Fruit": "banana",
                "Country": "italy",
                "Value": 1
            },
            {
                "Color": "yellow",
                "Fruit": "pineapple",
                "Country": "italy",
                "Value": 5
            },
            {
                "Color": "yellow",
                "Fruit": "mango",
                "Country": "italy",
                "Value": 1
            }
        ],
        "values": [
            1,
            5
        ]
    }
}
*/

