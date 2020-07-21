// Problem 3
var intervalID
var cnt = 0;
var runningTime;
function CountDown(){
    if (cnt == 0){
        stopNoodle();
        alert(String(runningTime) + " minutes passed");
        return;
    }
    var element = document.getElementById('message');
    element.textContent = String(--cnt) + " seconds later";
}
function startNoodle() {
    runningTime = parseInt(document.getElementById("time").value);
    var element = document.getElementById("start");
    element.disabled = true;
    cnt = runningTime * 60;
    intervalID = setInterval(CountDown, 1000);
}

function stopNoodle() {
    var element = document.getElementById("start");
    element.disabled = false;
    clearInterval(intervalID);
}
