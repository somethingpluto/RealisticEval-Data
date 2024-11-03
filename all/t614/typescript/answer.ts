function calculateAverageDifference(numbers: number[]): number {
    // Check if the list is valid (at least 2 numbers)
    if (!numbers || numbers.length < 2) {
        return 0.0; // Not enough data to calculate differences
    }

    // Calculate differences from the previous data
    const differences: number[] = [];
    for (let i = 1; i < numbers.length; i++) {
        differences.push(numbers[i] - numbers[i - 1]);
    }

    // Calculate the average of the differences
    const sum = differences.reduce((acc, diff) => acc + diff, 0);
    return sum / differences.length;
}