// https://stackoverflow.com/questions/50434025/add-a-top-list-in-each-object-of-my-array
var myNewArray = []
var newObj = {}
var colors = []
var fruitNames = []

var myArray = [
    {Color:"red", Fruit:"apple", Country:"us", Value:1},
    {Color:"red", Fruit:"cherry", Country:"us", Value:1},
    {Color:"red", Fruit:"apple", Country:"italy", Value:1},
    {Color:"red", Fruit:"apple", Country:"italy", Value:2}, 
    {Color:"red", Fruit:"strawberry", Country:"italy", Value:2},                
    {Color:"red", Fruit:"cherry", Country:"italy", Value:1},
    {Color:"yellow", Fruit:"banana", Country:"us", Value:1},
    {Color:"yellow", Fruit:"banana", Country:"italy", Value:1},
    {Color:"yellow", Fruit:"pineapple", Country:"italy", Value:5},
    {Color:"yellow", Fruit:"mango", Country:"italy", Value:3},          
];

for(let obj of myArray) {
        var color = obj.Color;

        // Add color as key of obj that points list of objects of same color
        if(newObj[color] === undefined) {
            // Create new
            newObj[color] = {}
            newObj[color].fruits = []
            newObj[color].fruitNames = []

            colors.push(color)
            // console.log('Created')
            // console.log(newObj)
            newObj[color]['fruits'].push(obj)
            newObj[color].fruitNames.push(obj.Fruit)
            newObj[color]['values'] = [obj.Value]
            // console.log(newObj)
            // console.log(newObj[color]['fruits']['Country'])
        } else {
            // Push fruit
            newObj[color].fruits.push(obj);
            newObj[color]['fruitNames'].push(obj.Fruit)

            // Checking values (Creating a list of unique values)
            // if(newObj[color]['values'].indexOf(obj.Value) < 0) {
                newObj[color]['values'].push(obj.Value)
            // }
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

for(let color in newObj) {
    let item = {}
    item.Color = color
    item.Total = newObj[color]['fruits'].length
    topFruits = []

    var count = 2
    while(item.Total > 0 && count > 0) {
        let maxValue = newObj[color].values.reduce(function(accumulator, currentValue, currentIndex, array) {
            return Math.max(accumulator, currentValue)
        }) 
        console.log("Max Value", maxValue)

        // let maxIndex = newObj[color].values.indexOf(maxValue);
        // console.log("Max index", maxIndex)

        let maxIndex = newObj[color].values.indexOf(maxValue) 
        let maxFruitName = newObj[color].fruitNames[maxIndex]
        topFruits.push(maxFruitName)
        // while(maxIndex > -1) {
            console.log("Removing ", maxValue)
            newObj[color].values.splice(maxIndex, 1)
            newObj[color].fruitNames.splice(maxIndex, 1)
            // maxIndex = newObj[color].values.indexOf(maxValue)    
        // }

        // let maxFruitName = 
        // while( > -1) {
        //     console.log("Removing ", maxValue)
        //     maxIndex = newObj[color].fruitNames.indexOf(maxFruitName) 
        //     newObj[color].values.splice(maxIndex, 1)
        // }
        //newObj[color].values.splice(maxValue, 1) // Remove max value
        //newObj[color].fruitNames.splice(maxValue, 1) // // Remove fruit name (corresponding to max value)
        


        count -= 1;
    }
    
    item.top2 = "" + topFruits
    myNewArray.push(item)
}

console.log(myNewArray)
