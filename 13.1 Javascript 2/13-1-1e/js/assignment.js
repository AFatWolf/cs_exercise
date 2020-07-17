// Assignment 1
var cnt = 0;
function plus() {
    cnt++;
    var element = document.getElementById("count");
    element.textContent = String(cnt)
}

function minus() {
    cnt--;
    var element = document.getElementById("count");
    element.textContent = String(cnt);
}
