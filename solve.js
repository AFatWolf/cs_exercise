var strings = ['Information', 'Networking', 'for', 'Innovation', 'and', 'Design'];
var cnt = 0;

function updateTarget() {
    var str = strings[cnt];
    var element = document.getElementById('target');
    element.textContent = str;
    cnt++;
}