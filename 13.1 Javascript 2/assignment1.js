function abbrev(text){
    var s = ""
    for (var c of text){
        if (c == 'i' || c == 'u' || c == 'e' || c == 'a' || c == 'o') continue;
        s += c;
    }
    return s;
}
console.log(abbrev(`supermarket`))
console.log(abbrev("toyo university is wonderful"))
