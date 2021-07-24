// https://stackoverflow.com/questions/68508086/how-can-i-find-out-if-an-array-contains-a-certain-string/68508260#68508260

function getTheExactStrings(myarray, myname) {
    // Write a regular expression as per your need to match the substrings
    const regex = new RegExp(`.*(\\s+|^)${myname}(\\s+|$).*`);

    // Iterate over array items and try to return true/false using `test() method`
    return myarray.filter((name) => {
        return regex.test(name);
    });
}

// start
var mystring;
var myname = "Level 1-1";
var myarray = [
    "My Level 1-11 Ticket",
    "My Level 1-1 Ticket",
    "My Level 10-1 Ticket",
    "My Level 10-11 Ticket",
];

// Call the function to get result
console.log(getTheExactStrings(myarray, myname)); // [ 'My Level 1-1 Ticket' ]
  