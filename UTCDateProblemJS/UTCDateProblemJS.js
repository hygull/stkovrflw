// var birthday = new Date('August 19, 1975 23:15:30');
// var date1 = birthday.getDate();

// console.log(date1);
// expected output: 19

// var inputDateString = "Fri Nov 10 05:45:36 +0000 2017";
var inputDateString = "Fri Nov 10 23:45:36 +0000 2017";
var date = new Date(inputDateString);

console.log(date); // 2017-11-10T05:45:36.000Z

// .................. EXAMPLE 1 ..........................
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
console.log(utcDate.toISOString().split('T')[0]); // 2017-11-10

// .................. EXAMPLE 2 ..........................
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
console.log(utcDate2.toISOString().split('T')[0]); // 2017-11-10