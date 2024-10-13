function minRemovalsToMakeUnique(nums) {
    let numbers = [];
    let minimumDistinct = 0;
    for (let number of nums) {
        let index = numbers.indexOf(number);
        if (index !== -1) {
            minimumDistinct += 1;
            numbers.splice(index, 1);
        }
        numbers.push(number);
    }
    return minimumDistinct;
}