// All the comments inside function are for 
// inputDateStr: "Fri Nov 10 05:45:36 +0000 2017"
function getMyUTCDate(inputDateStr)
{
	var inputDateString = inputDateStr;
	var date = new Date(inputDateString);
	var dateArr = []; // To store 2 dates, simple one & full UTC one

	console.log(date); // 2017-11-10T05:45:36.000Z

	// ............... SIMPLE EXAMPLE ..........................
	var year = date.getFullYear();
	var month = date.getMonth();
	var day = date.getDate();
	var hours = date.getHours();
	var minutes = date.getMinutes()
	var seconds = date.getSeconds();

	console.log(year); 	// 2017
	console.log(month); // 10
	console.log(day); 	// 10
	console.log(hours); // 11
	console.log(minutes); // 15
	console.log(seconds); // 36

	utcDate = new Date(Date.UTC(year, month, day, hours, minutes, seconds));
	utcDateString = utcDate.toUTCString();
	console.log(utcDate); 		// 2017-11-10T11:15:36.000Z
	console.log(utcDateString); // Fri, 10 Nov 2017 11:15:36 GMT
	var dt1 = utcDate.toISOString().split('T')[0]
	dateArr.push(dt1)
	console.log(dt1); // 2017-11-10

	// .................. FULL UTC EXAMPLE ..........................
	var utcYear = date.getUTCFullYear();
	var utcMonth = date.getUTCMonth();
	var utcDay = date.getUTCDate();
	var utcHours = date.getUTCHours();
	var utcMinutes = date.getUTCMinutes()
	var utcSeconds = date.getUTCSeconds();

	console.log(utcYear);	// 2017
	console.log(utcMonth);	// 10
	console.log(utcDay);	// 10
	console.log(utcHours); 	// 5
	console.log(utcMinutes);// 45
	console.log(utcSeconds);// 36

	var utcDate2 = new Date(Date.UTC(utcYear, utcMonth, utcDay, utcHours, utcMinutes, utcSeconds));
	var utcDateString2 = utcDate2.toUTCString();
	console.log(utcDate2);			// 2017-11-10T05:45:36.000Z
	console.log(utcDateString2);	// Fri, 10 Nov 2017 05:45:36 GMT

	// Get UTC Date
	var dt2 = utcDate2.toISOString().split('T')[0]
	dateArr.push(dt2)
	console.log(dt2); // 2017-11-10

	return dateArr;
}

// Inputs
var inputDateString1 = "Fri Nov 10 05:45:36 +0000 2017";
var inputDateString2 = "Mon May 14 23:59:36 +0000 2018";

var dateArr1 = getMyUTCDate(inputDateString1);
var dateArr2 = getMyUTCDate(inputDateString2);

// Print dates
console.log(dateArr1); // [ '2017-11-10', '2017-11-10' ]
console.log(dateArr2); // [ '2018-05-15', '2018-05-14' ]