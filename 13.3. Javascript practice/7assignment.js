function combination(n,r){
    var res = 1;
    for (var i=1;i<=n;++i) res *= i;
    for (var i=1;i<=r;++i) res/=i;
    for (var i=1;i<=(n-r);++i) res/=i;
    return res;
}
console.log(combination(10,5));