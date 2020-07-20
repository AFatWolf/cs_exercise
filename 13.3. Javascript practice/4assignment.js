function print(name, score){
    return name + "'s grade is " + score;
}
function grade(name, score){
    if (score < 60) return print(name, "F");
    if (score < 70) return print(name, "D");
    if (score < 80) return print(name, "C");
    if (score < 90) return print(name, "B");
    return print(name, "A");
}
console.log(grade("David", 80));
console.log(grade("John", 7));    
console.log(grade("Parker", 36));  
console.log(grade("Smith", 98));  