function calculateAverageDifference(numbers) {
    // Check if the list is valid (at least 2 numbers)
    if (!numbers || numbers.length < 2) {
        return 0.0; // Not enough data to calculate differences
    }

    // Calculate differences from the previous data
    const differences = numbers.slice(1).map((num, i) => num - numbers[i]);

    // Calculate the average of the differences
    return differences.reduce((acc, curr) => acc + curr, 0) / differences.length;
}