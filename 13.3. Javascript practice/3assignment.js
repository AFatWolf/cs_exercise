var ans = 0;
for (var i = 1; i<100; ++i){
    if (i % 5 == 0 || i % 7 == 0) {
        ans += i;
    }
}
console.log(ans);