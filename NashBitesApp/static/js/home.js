//Event handler to manage vendor view map


// Declare global variables
var map;
var geocoder
var originAddress;


// Function initializes and adds the Nashville map w/o marker
function initMap() {

  geocoder = new google.maps.Geocoder();

  // The location of Nashville, TN
  const nashville = { lat: 36.174465, lng: -86.767960 };

  // The map, centered at Nashville, TN
  map = new google.maps.Map(
    document.getElementById('home-map'), { zoom: 12, center: nashville });

  // setMarkers(map)

}

// Function gets locations database and . . .
function getDestinations() {
  // Fetch location_list view which returns Location data
  fetch('/location/')

    // Then take the returned data and convert to JSON
    .then(response => {
      return response.json()
    })
    .then(data => {

      // Sort data by timestamp in descending order
      data_sort = data.sort(function (a, b) {

        var timeA = new Date(b.timestamp).getTime();
        var timeB = new Date(a.timestamp).getTime();
        return timeA > timeB ? 1 : -1;
      })
      return data_sort
    })
    .then(data_sort => {

      var seen = [];
      var destinations = [];

      // Loop thru sorted data
      for (var i = 0; i < data_sort.length; i++) {


        //If data is not in the array named "seen"
        if (!seen.includes(data_sort[i].vendor_id)) {

          // Add current address to the 'keep' array
          destinations.push([
            data_sort[i].address,
            data_sort[i].latitude,
            data_sort[i].longitude
          ]);

          // Add vendor id to the seen array
          seen.push(data_sort[i].vendor_id);

        }
      }
      console.log(destinations)
      return destinations;
    })
    .then(destinations => {


      // Loop thru destinations and add marker to google map
      for (var i = 0; i < destinations.length; i++) {
        var destination = destinations[i];
        var marker = new google.maps.Marker({
          position: { lat: destination[1], lng: destination[2] },
          map: map,
          title: destination[0]

        })
        marker.setMap(map);
      }
    })
}

// Click handler function for encoding search input
function codeAddress() {

  var address = document.getElementById('address').value;
  geocoder.geocode({ 'address': address }, function (results, status) {

    if (status == 'OK') {

      map.setCenter(results[0].geometry.location);
      originAddress = results[0].formatted_address;
      console.log("Origin: ", originAddress);
      getDestinations();

    } else {
      alert('Geocode was not successful for the following reason: ' + status);
    }
  });
}




