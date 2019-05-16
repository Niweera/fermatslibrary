var bigInt = require("big-integer");


function checkP(){
    let number = 4;
    while (true) {
        if (bigInt(number).isPrime()){
            console.log(number);
            var y = bigInt(number).pow(number);
            var x = bigInt(y).plus(2);
            if (bigInt(x).isPrime()){
                console.log("this is it; x: " + x + " number: " + number);
                break;
            }else{
                number = number + 1;
            }
        }else{
            number = number + 1;
        }
      }
}



checkP();