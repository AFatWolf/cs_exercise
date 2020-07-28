function count() {
	var inputX = document.getElementById('input-x');
	var x = inputX.value;
	var inputC = document.getElementById('input-c');
	var c = inputC.value;
	// alert(x);
	var num = 0;
	for (var i=0;i<x.length;++i){
		num += (c == x[i]);
	}
  
	var outputX = document.getElementById('output-x');
	outputX.textContent = x;
	var outputC = document.getElementById('output-c');
	outputC.textContent = c;
	var outputNum = document.getElementById('output-num');
	outputNum.textContent = String(num);
  }