function voting_right(age, year){
    var voting_age = 18 + (year < 2016) * 2;
    var element = document.getElementById("result");
    element.textContent = (age >= voting_age ? "You have right to vote" : "You have no right to vote");
}