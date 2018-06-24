var arrOfArr = [
    ['one', 1],
    ['two', 2],
    ['three', 3]
]

var newMap = new Map(arrOfArr)
newMap

var iteratorObj = newMap[Symbol.iterator]();

// Printing keys and values
for (let item of iterator1) {
console.log(item[0], item[1])


for (let item of iterator) {
console.log(item[0], item[1])

for (let item of iteratorObj) {
console.log(item[0], item[1])
}

console.log(map1.get('bar'))
