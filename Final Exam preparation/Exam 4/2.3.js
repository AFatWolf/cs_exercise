function euro_to_dollar() {
    var input = document.getElementById('input');
    var euro = parseInt(input.value, 10);
    var dollar = euro * 132.88 / 113.08;
    var elemEuro = document.getElementById('euro');
    elemEuro.textContent = String(euro);
    var elemDollar = document.getElementById('dollar');
    elemDollar.textContent = String(dollar);
    }
function dollar_to_euro() {
    var input = document.getElementById('input');
    var dollar = parseInt(input.value, 10);
    var euro = dollar*113.08/132.88;
    var elemEuro = document.getElementById('euro');
    elemEuro.textContent = String(euro);
    var elemDollar = document.getElementById('dollar');
    elemDollar.textContent = String(dollar);
}