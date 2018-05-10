The specified JSON was not in valid form as it is missing two `}` (curley braces) and one `]` (left big bracket). I visited https://jsoneditoronline.org and corrected it.


> **Note:** I have saved the corrected **JSON** file `paws.json` at [this web page](https://gist.github.com/hygull/aeb34b1d8808c440117f0a4f8e960e62) on **Github**.
Please use that one.

Finally, try the below code on your server.
> **Note:** I am Django developer so I used **Django** to serve the page. It worked fine.

    <!doctype html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <title>Read JSON and process</title>
    <script src="https://code.jquery.com/jquery-1.10.2.js"></script>
    </head>
    <body>

    <!-- Populate all the photos and descriptions here-->
    <div id='photos'>
    </div>

    <!-- Code to grab pets/photos and creating div elements -->
    <script type="text/javascript">
    $.getJSON("paws.json' %}", function(data){
          // console.log("It's great to see you here.");
          // console.log(data);
          var photoHTML = ''

          // Storing pets to a variable named pets
          var pets = data.petfinder.pets.pet; // Here pets(in paws.json) has 2 items

          // Loop through pets array
          $.each(pets, function(index, pet){
              // console.log("PETS INDEX :", index);
              // Storing photos to a varibale named photos
              var photos = pet.media.photos.photo;
              // Loop through photos array
              $.each(photos, function(index, photo){
                  // console.log("PHOTO INDEX ", index);
                  // console.log(photo.$t)
                  photoHTML += '<div class="picbox"><figure><img src="' + photo.$t + '" class="frame"><figcaption>' + pet.description.$t + '</figcaption></figure></div>';
              })
          })
          console.log(photoHTML)
          $('#photos').html(photoHTML);
    })
    </script>

    </body>
    </html>


That's it.