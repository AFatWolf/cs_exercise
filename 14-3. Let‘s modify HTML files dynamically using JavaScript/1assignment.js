function startProcessing(){
    var element = document.getElementById("result");
    element.innerHTML = "<p>Contents written in JavaScript</p><p>Letter only</p>";
}
function display(){
    var message = document.getElementById("result").innerHTML;
    var element = document.getElementById("new-post");
    element.value = message;
}