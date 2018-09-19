//Event handler to manage vendor view map


// Declare global variables
var map;
var marker; 
var infowindow;
var messagewindow;

var addressEl = document.getElementById('id_address')
var latEl = document.getElementById('id_latitude')
var longEl = document.getElementById('id_longitude')

// Function initializes and adds the Nashville map w/ marker
function initMap() {

  // The location of Nashville, TN
  const nashville = {lat: 36.174465, lng: -86.767960};

  // The map, centered at Nashville, TN
  map = new google.maps.Map(
      document.getElementById('vendor-map'), {zoom: 12, center: nashville});

  // The marker, positioned at Nashville, TN
  marker = new google.maps.Marker({
    position: nashville, 
    map: map,
    draggable: true,
  });

  // Event to get marker position on dragend into form fields.  Geocoding occurs in vendor.py function
  google.maps.event.addListener(marker, 'dragend', function(evt){
    var lat, long, address;
    
    lat = marker.getPosition().lat();
    long = marker.getPosition().lng();
    console.log(lat, long)
    
    // 
    var geocoder = new google.maps.Geocoder();

    geocoder.geocode({ latLng: marker.getPosition() }, function(result, status){
      if('OK' === status){
        console.log(result)
        address = result[0].formatted_address;
        addressEl.value = address
        latEl.value = lat;
        longEl.value = long;

      } else { 
        alert('Geocode was not successful for the following reason: ' + status)
      }

    })
  })
}

