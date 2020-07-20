function triangle(n){
    for(var i = 8;i>=1;--i){
        var ans = "";
        for(var j=0;j<Math.floor(i/2);++j) ans += "*+";
        ans += (i % 2 ? "*" : "");
        console.log(ans);
    }
}
triangle(8);