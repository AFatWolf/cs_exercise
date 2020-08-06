// Sample 1
function displayCoordinate(result) {
  if (result == null) {
    return;
  }
  var lat = document.getElementById('lat');
  var lon = document.getElementById('lon');
  lat.textContent = result.lat;
  lon.textContent = result.lng;
}

function getCoordinate() {
  var inputAddress = document.getElementById('input-address');
  callGeocodingAPI(inputAddress.value, displayCoordinate);
}

// Sample 2
function displayWeather(result) {
  var city = document.getElementById('city');
  var weather = document.getElementById('weather');
  var temperature = document.getElementById('temperature');
  var humidity = document.getElementById('humidity');
  var pressure = document.getElementById('pressure');

  city.textContent = result.city;
  weather.textContent = result.weather;
  temperature.textContent = result.temperature;
  humidity.textContent = result.humidity;
  pressure.textContent = result.pressure;
}

function getWeather() {
  var inputLatitude = document.getElementById('input-lat');
  var inputLongitude = document.getElementById('input-lon');
  callWeatherAPI(inputLatitude.value, inputLongitude.value, displayWeather);
}

// Sample 3
var map;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: { lat: 35.7804643, lng: 139.7151025 },
    zoom: 15
  });
}

function setMapCenter() {
  var inputLatitude2 = document.getElementById('input-lat2');
  var inputLongitude2 = document.getElementById('input-lon2');
  map.setCenter({ lat: Number(inputLatitude2.value), lng: Number(inputLongitude2.value) });
}
