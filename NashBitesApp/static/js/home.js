//Event handler to manage vendor view map


// Declare global variables
var map;
var geocoder
var marker; 
var infowindow;
var messagewindow;
var originAddress;
var destinationAddress;


// Function initializes and adds the Nashville map w/o marker
function initMap() {

  geocoder = new google.maps.Geocoder();

  // The location of Nashville, TN
  const nashville = {lat: 36.174465, lng: -86.767960};

  // The map, centered at Nashville, TN
  map = new google.maps.Map(
      document.getElementById('home-map'), {zoom: 12, center: nashville});
  
    }
  
  // Click handler function for encoding search input
  function codeAddress() {

    var address = document.getElementById('address').value;
    geocoder.geocode( { 'address': address}, function(results, status) {

    if (status == 'OK') {

      map.setCenter(results[0].geometry.location);
      originAddress = results[0].formatted_address;
      console.log("Origin: ", originAddress)

    } else {

      alert('Geocode was not successful for the following reason: ' + status);

    }
  });
}

// Fetch location_list view which returns Location data
fetch('/location/')

// Then take the returned data and convert to JSON
.then(response => {
    return response.json()
})
.then(data => {
    console.log(data)
})


