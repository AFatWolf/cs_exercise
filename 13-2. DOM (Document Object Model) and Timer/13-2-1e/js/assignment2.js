// Problem 2
function calcTax() {
    var raw_price = Number(document.getElementById("price-without-tax").value);
    var tax_rate = Number(document.getElementById("tax-rate").value);
    var price = raw_price + raw_price * tax_rate/100;
    // alert(price);
    var element = document.getElementById("price");
    element.textContent = String(price) + " ";
    element = document.getElementById("tax");
    element.textContent = String(raw_price * tax_rate/100) + " ";
}
