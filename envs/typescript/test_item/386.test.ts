function sumEvenNumbers(numbers: number[]): number {
    return numbers.reduce((sum, current) => current % 2 === 0 ? sum + current : sum, 0);
}

