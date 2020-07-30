var cnt;
var intervalId;

function updateMessage() {
    var elem = document.getElementById('message');
    cnt++;
    elem.innerHTML = '<b>Elapsed Time:</b> ' + cnt + ' seconds';
}

function start() {
    cnt = 0;
    intervalId = setInterval(updateMessage, 1000);
}

function stop() {
    clearInterval(intervalId);
    var elem = document.getElementById('message');
    elem.innerHTML = '<b>Elapsed Time:</b> 0 seconds';
}