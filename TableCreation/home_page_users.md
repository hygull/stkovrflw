Based on the requirement, I copied Bootstrap3 based HTML code from [w3schools.com - Bootstrap3 Tables (Hover)](https://www.w3schools.com/bootstrap/tryit.asp?filename=trybs_table_hover&stacked=h) page and wrote javascript so that It could fulfill your requirement.

I have written the javascript code by thinking that I am going to create a dynamic table of users based on the user input (which I will accept from using **prompt()**). The code

* asks for integer input **n** (Number of users that we want to create).

* asks names for **n** users.

* asks to re-enter input **n** (if you don't eneter proper integer) or name of users (if you leave user's name blank).

Please have a look at the below gif image (Full working code is also available which you can copy and modify).


Finally, you can copy and try to execute the below HTML code in your browser.

    <!DOCTYPE html>
    <html lang="en">
    <head>
      <title>All Users - Example</title>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
      <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
      <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    </head>
    <style type="text/css">
      td {
        font-family: tahoma;
        color: blue;
      }
      h1 {
        color: green;
      }
      p {
        color: blue;
        font-family: tahoma;
      }
    </style>
    <body>

    <!-- HTML CODE COPIED FROM: https://www.w3schools.com/bootstrap/tryit.asp?filename=trybs_table_hover&stacked=h -->
    <center>
        <h1>All Users</h1> 
    </center>

    <div class="container text-center" id='table'>
      <div class="col-xs-12 col-md-4 col-md-offset-4 col-lg-4 col-lg-offset-4">
        <p>Currently, no user(s) found, you need to create it</p>
        <br>
        <button class='btn btn-success' onclick="createUsersTable()">Create now</button>   
      </div>    
    </div>


    <script type="text/javascript">
      // Coded: 20 May 2018, Sun
      // Note: You can uncomment the lines if you want table header
      function createUsersTable() {
        var n = prompt('Enter number of users that you want to create.');
        var tableHtmlStart = '<table class="table table-hover">' +
          // '<thead>' +
          //   '<tr>' +
          //     '<th style="text-align:center">User(s)</th>' +
          //   '</tr>' +
          // '</thead>' +
          '<tbody>'

        var users = ""
        var tableHtmlEnd = "</tbody></table>"

        console.log(n)

        if(n === null) {
          // If user cancels
          alert("You cancelled")
          document.getElementById("table").innerHTML = "You cancelled"
        } else {
            if(n === '') {
              alert("Don't leave blank, please enter an integer")
              createUsersTable()
            } else {
              n = parseInt(n);
              if(!Number.isInteger(n)){
                alert("Input should be an integer, please enter an integer")
                createUsersTable()
              } else { // If n is an integer
                if(n < 0) {
                  alert("Please enter a +ve integer, you entered: "+ n)
                  createUsersTable()
                } else { // If the user inputs a proper integer > 0
                  for(var i = 0; i < n; ){ // Taking user names using prompt()
                    var user = prompt("Enter the name of USER " + (i + 1) + ":")
                    if(user == null) {
                      alert("You cancelled, please enter correct name of USER" + (i + 1))
                    } else {
                      if(user == ''){
                        alert("Username can't be blank, please enter correct name of USER" + (i + 1))
                      } else {
                        console.log("User " + (i + 1) + " successfully added")
                        users += '<tr><td>' + user + '</td></tr>'
                        i = i + 1;
                      }
                    }
                  }

                  // Setting innerHTML of div with id 'table'
                  document.getElementById("table").innerHTML = tableHtmlStart + users + tableHtmlEnd;
                }
              }
            }
          }
        }
    </script>
    </body>
    </html>


Thanks.