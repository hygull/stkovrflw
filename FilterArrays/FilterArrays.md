**@Palani**, I'll suggest you to use an object to gather all the required information.
Please have a look at the below code and let me know any suggestions/modifications if you need. 


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
        var arr = [obj["year"], obj["month"], obj["day"], obj["hour"], obj["interval"]];

        var newObj = {
            "x": arr.join(", "),
            "y": timeData["count"],
        }

        if(newTimeData[obj["method"] + "Array"]) { // method found
            newTimeData[obj["method"] + "Array"].push(newObj)
        } else { // method not found
            newTimeData[obj["method"] + "Array"] = [newObj]
        }
    }

    // PRETTY PRINTING OBJECT 
    console.log(JSON.stringify(newTimeData, undefined, 4))
    /*...
            {
                "200Array": [
                    {
                        "x": "2018, 6, 11, 12, 45",
                        "y": 1
                    },
                    {
                        "x": "2016, 11, 11, 17, 10",
                        "y": 47
                    }
                ],
                "404Array": [
                    {
                        "x": "2016, 11, 11, 16, 50",
                        "y": 5
                    }
                ]
            }
    ...*/


    // PRETTY PRINTING ARRAY POINTED BY '200Array' key
    console.log(JSON.stringify(newTimeData["200Array"], undefined, 4))
    /*...
            [
                {
                    "x": "2018, 6, 11, 12, 45",
                    "y": 1
                },
                {
                    "x": "2016, 11, 11, 17, 10",
                    "y": 47
                }
            ]
    ...*/

    // PRETTY PRINTING ARRAY POINTED BY '404Array' key
    console.log(JSON.stringify(newTimeData["404Array"], undefined, 4))
    /*...
            [
                {
                    "x": "2016, 11, 11, 16, 50",
                    "y": 5
                }
            ]
    ...*/



### Output &raquo;

    H:\RishikeshAgrawani\Projects\Sof\FilterArrays>node FilterArrays.js
    {
        "200Array": [
            {
                "x": "2018, 6, 11, 12, 45",
                "y": 1
            },
            {
                "x": "2016, 11, 11, 17, 10",
                "y": 47
            }
        ],
        "404Array": [
            {
                "x": "2016, 11, 11, 16, 50",
                "y": 5
            }
        ]
    }
    [
        {
            "x": "2018, 6, 11, 12, 45",
            "y": 1
        },
        {
            "x": "2016, 11, 11, 17, 10",
            "y": 47
        }
    ]
    [
        {
            "x": "2016, 11, 11, 16, 50",
            "y": 5
        }
    ]