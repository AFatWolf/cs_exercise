function max_len(xs){
    var ans = 0;
    for (var x of xs) ans = Math.max(ans, x.length);
    return ans;
}
console.log(max_len(['I', "have", "a", "pen"]))
console.log(max_len(['I', "have", "a", "apple"]))