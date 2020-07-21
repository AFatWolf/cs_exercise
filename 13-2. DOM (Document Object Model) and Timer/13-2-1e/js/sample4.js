// Sample 4-1
function showDialogTimeout() {
  alert('Hello');
}

var timeoutId;
function startTimeout() {
  timeoutId = setTimeout(showDialogTimeout, 5000);
}

function stopTimeout() {
  clearTimeout(timeoutId);
}

// Sample 4-2
var cnt;
function updateContentInterval() {
  cnt++;
  var element = document.getElementById('count');
  element.textContent = String(cnt);
}

var intervalId;
function startInterval() {
  cnt = 0;
  intervalId = setInterval(updateContentInterval, 1000);
}

function stopInterval() {
  clearInterval(intervalId);
}
