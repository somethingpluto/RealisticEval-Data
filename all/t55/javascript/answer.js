function minRemovalsToMakeUnique(nums) {
    let numbers = [];
    let minimumDistinct = 0;
    for (let number of nums) {
        if (numbers.includes(number)) {
            minimumDistinct += 1;
            let index = numbers.indexOf(number);
            numbers.splice(index, 1);
        }
        numbers.push(number);
    }
    return minimumDistinct;
}