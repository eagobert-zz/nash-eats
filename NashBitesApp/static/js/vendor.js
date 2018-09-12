//Event handler to manage vendor view map


// Declare global variables
var map;
var marker; 
var infowindow;
var messagewindow;

// Function initializes and adds the Nashville map w/ marker
function initMap() {

  // The location of Nashville, TN
  const nashville = {lat: 36.174465, lng: -86.767960};

  // The map, centered at Nashville, TN
  map = new google.maps.Map(
      document.getElementById('vendor-map'), {zoom: 10, center: nashville});

  // The marker, positioned at Nashville, TN
  marker = new google.maps.Marker({
    position: nashville, 
    map: map,
    draggable: true,
  });

  // Event to get marker position on dragend
  google.maps.event.addListener(marker, 'dragend', function(evt){
    var lat, long, address;
    
    lat = marker.getPosition().lat();
    long = marker.getPosition().lng();
    console.log("I am dragged!")
    console.log(lat, long)
    
  })
}

