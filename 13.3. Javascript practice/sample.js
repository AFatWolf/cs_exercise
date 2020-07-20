var count = 0;
function CountUp(){
    count = (count + 1) % 11;
}
function DisplayCount(){
    alert(count);
}
function HOGE(){
    var ans = "";
    for (var i = 0; i < count;++i) ans += "HOGE";
    alert(ans);
}
