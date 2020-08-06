function addition() {
	var elem1 = document.getElementById('op1');
	var x = parseFloat(elem1.value);
	var elem2 = document.getElementById('op2');
	var y = parseFloat(elem2.value);
  
	var elem3 = document.getElementById('result');
	elem3.textContent = String(x + y);
  }