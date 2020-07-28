var intervalID;
var curPos = 0;
function tick(){
    if (curPos >= 347) {
        clearInterval(intervalID);
        return;
    }
    var element = document.getElementById("object");
    var box = document.getElementById("container");
    curPos++;
    // alert(curPos.toString() + "px");
    element.style.top = element.style.left = curPos.toString() + "px"; 
}
function startAnimation(){
    intervalID = setInterval(tick, 5);
}