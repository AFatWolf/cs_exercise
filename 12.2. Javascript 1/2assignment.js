function result(p1, p2) {
    if (p1 > p2)
        return "win"
    if (p1 == p2)
        return "draw"
    return "lose"
}

console.log(result(1, 10));
console.log(result(1, 1));
console.log(result(10, 1));

function permutation(n, k) {
    var ans = 1;
    for (var i=n-k+1;i<=n;++i) ans *= i;
    return ans;
}

var p = permutation(10, 3);
console.log(p);