function getAverage(array) { // returns the average of a list of numbers, generated by chatgpt
    let sum = 0;
    for (let i = 0; i < array.length; i++) {
        sum += array[i];
    }
    return sum / array.length;
}