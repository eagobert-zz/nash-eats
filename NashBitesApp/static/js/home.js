//Event handler to manage vendor view map


// Declare global variables
var map;
var geocoder
var marker; 
var infowindow;
var messagewindow;

// Function initializes and adds the Nashville map w/o marker
function initMap() {

  geocoder = new google.maps.Geocoder();
  
  // The location of Nashville, TN
  const nashville = {lat: 36.174465, lng: -86.767960};

  // The map, centered at Nashville, TN
  map = new google.maps.Map(
      document.getElementById('home-map'), {zoom: 12, center: nashville});
  
    }
    
  function codeAddress() {
      var address = document.getElementById('address').value;
      geocoder.geocode( { 'address': address}, function(results, status) {
    if (status == 'OK') {
      console.log(results)
      map.setCenter(results[0].geometry.location);
      var marker = new google.maps.Marker({
          map: map,
          position: results[0].geometry.location
      });
    } else {
      alert('Geocode was not successful for the following reason: ' + status);
    }
  });
}