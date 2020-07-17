// Sample 2-1
function showDialog() {
  alert('Hello');
}

// Sample 2-2
var count = 0;
function countClick() {
  count++;
  var element = document.getElementById('count');
  element.textContent = String(count);
}
