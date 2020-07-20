fortune = ["大吉","吉","中吉","小吉", "末吉","凶"];
function fortune_telling(ymd){
    return fortune[ymd % 6];
};
function display_fortune(){
    var ymd = parseInt(document.getElementById("birthday").value);
    // alert(ymd);
    var element = document.getElementById("result");
    element.textContent = fortune_telling(ymd);
}