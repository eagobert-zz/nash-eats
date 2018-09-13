//Event handler to manage vendor view map


// Declare global variables
var map;
var marker; 
var infowindow;
var messagewindow;

var searchEl = document.getElementById('search-input')

// Function initializes and adds the Nashville map w/o marker
function initMap() {

  // The location of Nashville, TN
  const nashville = {lat: 36.174465, lng: -86.767960};

  // The map, centered at Nashville, TN
  map = new google.maps.Map(
      document.getElementById('home-map'), {zoom: 12, center: nashville});

}