// https://stackoverflow.com/questions/50434025/add-a-top-list-in-each-object-of-my-array

var newObj = {}

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

for(let obj of myArray) {
        // Add color as key of obj that points list of objects of same color
        if(newObj[ obj.Color] === undefined) {
            // Create new
            newObj[obj.Color] = [obj]
            newObj['values'] = [obj.Value]
        } else {
            // Push
            newObj[obj.Color].push(obj)

            // Checking values (Creating a list of unique values)
            if(newObj['values'].indexOf(obj.Value) < 0) {
                newObj['values'].push(obj.Value)
            } else {
                console.log("Skipping ", obj.Value)
            }
        }
}

console.log(newObj)
/*
{ red:
   [ { Color: 'red', Fruit: 'apple', Country: 'us', Value: 1 },
     { Color: 'red', Fruit: 'cherry', Country: 'us', Value: 1 },
     { Color: 'red', Fruit: 'apple', Country: 'italy', Value: 1 },
     { Color: 'red', Fruit: 'apple', Country: 'italy', Value: 2 },
     { Color: 'red', Fruit: 'strawberry', Country: 'italy', Value: 2 },
     { Color: 'red', Fruit: 'cherry', Country: 'italy', Value: 1 } ],
  yellow:
   [ { Color: 'yellow', Fruit: 'banana', Country: 'us', Value: 1 },
     { Color: 'yellow', Fruit: 'banana', Country: 'italy', Value: 1 },
     { Color: 'yellow',
       Fruit: 'pineapple',
       Country: 'italy',
       Value: 5 },
     { Color: 'yellow', Fruit: 'mango', Country: 'italy', Value: 1 } ] }
*/

