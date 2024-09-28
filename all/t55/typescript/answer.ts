function minRemovalsToMakeUnique(nums: number[]): number {
    const numbers: number[] = [];
    let minimumDistinct = 0;

    for (const number of nums) {
        if (numbers.includes(number)) {
            minimumDistinct += 1;
            numbers.splice(numbers.indexOf(number), 1);
        }
        numbers.push(number);
    }

    return minimumDistinct;
}