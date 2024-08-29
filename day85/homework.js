function manualFilter(callback, array) {
    let resultArray = [];
    for (let i = 0; i < array.length; i++) {
        if (callback(array[i])) {
            resultArray.push(array[i]);
        }
    }

    return resultArray;
}

function isOdd(num) {
    return num % 2 !== 0;
}

let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let oddNumbers = manualFilter(isOdd, numbers);
console.log(oddNumbers);
