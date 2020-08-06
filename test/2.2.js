function calculate() {
    var inputT = document.getElementById('input-temperature');
    var inputH = document.getElementById('input-humidity');
    var checkbox = document.getElementById('input-text');
    var t = parseFloat(inputT.value);
    var h = parseFloat(inputH.value);
  
    var di = 0.81*t + 0.01*h*(0.99*t - 14.3) + 46.3;

    var result = String(di);
  
    if(checkbox.checked) {
        var message = "";
        if (di >= 80) message = "(Uncomfortable)";
        else if (di >= 75) message = "(Slightly uncomfortable)";
        result += message;
    } 
  
    var spanResult = document.getElementById('di');
    spanResult.textContent = result;
  }