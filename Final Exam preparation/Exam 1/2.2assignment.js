function calculate() {
    var inputA = document.getElementById('in-a');
    var inputB = document.getElementById('in-b');
    var inputC = document.getElementById('in-c');
    var spanA = document.getElementById('a');
    var spanB = document.getElementById('b');
    var spanC = document.getElementById('c');
    var spanArea = document.getElementById('area');
    var a = parseFloat(inputA.value);
    var b = parseFloat(inputB.value);
    var c = parseFloat(inputC.value);
    var p = (a+b+c)/2; 
    var area = Math.sqrt(p*(p-a)*(p-b)*(p-c));
    alert(area);
    spanA.textContent = a;
    spanB.textContent = b;
    spanC.textContent = c;
    spanArea.textContent = area;
}