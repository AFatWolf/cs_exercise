function check() {
    var inputA = document.getElementById('input-a');
    var inputB = document.getElementById('input-b');
    var inputC = document.getElementById('input-c');
    var a = parseFloat(inputA.value);
    var b = parseFloat(inputB.value);
    var c = parseFloat(inputC.value);
    if (a == 0) {
        alert('Error.');
        return;
    }
    var n;
    var delta = b*b - 4*a*c;
    if (delta < 0) n = 0;
    else if (delta == 0) n = 1;
    else n = 2;
    // alert(delta);
    var paramA = document.getElementById('param-a');
    paramA.textContent = a;
    var paramB = document.getElementById('param-b');
    paramB.textContent = b;
    var paramC = document.getElementById('param-c');
    paramC.textContent = c;
    var result = document.getElementById('result');
    result.textContent = n;
}