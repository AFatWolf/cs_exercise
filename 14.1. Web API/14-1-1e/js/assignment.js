var map;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: { lat: 35.7804643, lng: 139.7151025 },
    zoom: 15
  });
}

function findWeather() {
  // 1. Try to retrieve latitude and longitude from address by using Geocoding API.
  // When the coorinate is retrieved, displayCoordinate should be called.
  var inputAddress = document.getElementById('input-address');
  callGeocodingAPI(inputAddress.value, displayCoordinate);

}

function displayCoordinate(result) {
  // 2. Display the coordinate.

  // 3. Then, find the weather of the coordinate using OpenWeatherMap.
  // When the weather is retrieved, displayWeather should be called.

  // 4. Set the map center.
  if (result == null) {
    return;
  }
  var lat = document.getElementById('latitude');
  var lon = document.getElementById('longitude');
  lat.textContent = result.lat;
  lon.textContent = result.lng;
  var latVal = Number(result.lat);
  var lonVal = Number(result.lng);
  callWeatherAPI(latVal, lonVal, displayWeather);
  // set map center
  map.setCenter({ lat: latVal, lng: lonVal });
  // 

}

function displayWeather(result) {
  // 5. Display the weather.
  var city = document.getElementById('city');
  var weather = document.getElementById('td-weather');
  var temperature = document.getElementById('td-temperature');
  var humidity = document.getElementById('td-humidity');
  var pressure = document.getElementById('td-pressure');

  city.textContent = result.city;
  weather.textContent = result.weather;
  temperature.textContent = result.temperature;
  humidity.textContent = result.humidity;
  pressure.textContent = result.pressure;
}
