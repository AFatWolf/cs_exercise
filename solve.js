function pow(x, y){
    var ans = 1;
    for (var i = 1; i <= y; ++i) ans *= x;
    return ans;
}
console.log(pow(2,3));
console.log(pow(3,4));
console.log(pow(4,5));