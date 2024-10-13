function minRemovalsToMakeUnique(nums: number[]): number {
    let numbers: Set<number> = new Set();
    let minimumDistinct: number = 0;

    for (let number of nums) {
        if (numbers.has(number)) {
            minimumDistinct += 1;
        } else {
            numbers.add(number);
        }
    }

    return minimumDistinct;
}