let i = 1;
while (i <= 10) {
    console.log(i);
    i++;
}




let i = 2;
while (i <= 20) {
    console.log(i);
    i += 2;
}




let i = 10;
while (i >= 1) {
    console.log(i);
    i--;
}





let sum = 0;
let i = 1;
while (sum <= 100) {
    sum += i;
    i++;
}
console.log("Sum:", sum);





let i = 1;
while (i <= 10) {
    console.log(`5 x ${i} = ${5 * i}`);
    i++;
}





let i = 10;
while (i >= 0) {
    console.log(`Countdown: ${i}`);
    i--;
}






let input;
while (input !== "exit") {
    input = prompt("Enter something (type 'exit' to stop):");
    console.log("You entered:", input);
}






let i = 1;
while (i <= 10) {
    console.log(`${i}^2 = ${i * i}`);
    i++;
}





let num = 1;
while (num <= 1000) {
    console.log(num);
    num *= 2;
}





let i = 1;
while (i < 20) {
    console.log(i);
    i += 2;
}






for (let i = 1; i <= 10; i++) {
    console.log(i);
}






for (let i = 2; i <= 20; i += 2) {
    console.log(i);
}






for (let i = 10; i >= 1; i--) {
    console.log(i);
}





let sum = 0;
for (let i = 1; i <= 10; i++) {
    sum += i;
}
console.log("Sum:", sum);






for (let i = 1; i <= 10; i++) {
    console.log(`5 x ${i} = ${5 * i}`);
}




let str = "Hello, world!";
for (let i = 0; i < str.length; i++) {
    console.log(str[i]);
}





let factorial = 1;
let num = 5;
for (let i = 1; i <= num; i++) {
    factorial *= i;
}
console.log("Factorial:", factorial);





for (let i = 0; i <= 50; i++) {
    if (i % 5 === 0) continue;
    console.log(i);
}






let squares = [];
for (let i = 1; i <= 10; i++) {
    squares.push(i * i);
}
console.log(squares);





let total = 0;
for (let i = 0; i < 5; i++) {
    total += i;
}
console.log("Total: " + total);






let age = 18;
if (age >= 18) {
    console.log("You are an adult.");
} else {
    console.log("You are a minor.");
}





let score = 75;
if (score >= 90) {
    console.log("A");
} else if (score >= 80) {
    console.log("B");
} else if (score >= 70) {
    console.log("C");
} else if (score >= 60) {
    console.log("D");
} else {
    console.log("F");






let number = 10;
if (number % 2 === 0) {
    console.log("Even");
} else {
    console.log("Odd");
}





let temp = 30;
if (temp > 30) {
    console.log("Hot");
} else if (temp >= 20) {
    console.log("Warm");
} else {
    console.log("Cold");
}






let isMember = true;
let price = isMember ? 10 : 20;
console.log("Price: $" + price);





let a = 5;
let b = 10;
if (a > b) {
    console.log("a is greater than b");
} else {
    console.log("b is greater than or equal to a");
}





let c = 7;
if (c % 3 === 0 && c % 5 === 0) {
    console.log("FizzBuzz");
} else if (c % 3 === 0) {
    console.log("Fizz");
} else if (c % 5 === 0) {
    console.log("Buzz");
} else {
    console.log(c);
}





let x = 5;
if (x < 10) {
    console.log("x is less than 10");
} else if (x > 10) {
    console.log("x is greater than 10");
} else {
    console.log("x is 10");
}





let time = 14;
if (time < 12) {
    console.log("Good morning");
} else if (time < 18) {
    console.log("Good afternoon");
} else {
    console.log("Good evening");
}





let trafficLight = "red";
if (trafficLight === "green") {
    console.log("Go");
} else if (trafficLight === "yellow") {
    console.log("Slow down");
} else if (trafficLight === "red") {
    console.log("Stop");
} else {
    console.log("Invalid traffic light color");
}


