var timeDataArr = [
    {
        "_id": {
            "year": 2018,
            "month": 6,
            "day": 11,
            "hour": 12,
            "interval": 45,
            "method": "200"
        },
        "count": 1
    },
    {
        "_id": {
            "year": 2016,
            "month": 11,
            "day": 11,
            "hour": 16,
            "interval": 50,
            "method": "404"
        },
        "count": 5
    },
    {
        "_id": {
            "year": 2016,
            "month": 11,
            "day": 11,
            "hour": 17,
            "interval": 10,
            "method": "200"
        },
        "count": 47
    }
]

// An object that maps 'method' to its related data array
var newTimeData = {}

for(var timeData of timeDataArr) {
    var obj = timeData["_id"];
    var newObj = {
        "x": "" + obj["year"] + obj["month"] + obj["day"] + obj["hour"] + obj["interval"],
        "y": timeData["count"],
    }

    if(newTimeData[obj["method"]]) { // method found
        newTimeData[obj["method"] + "Array"].push(newObj)
    } else { // method not found
        newTimeData[obj["method"] + "Array"] = [newObj]
    }
}

console.log(newTimeData)