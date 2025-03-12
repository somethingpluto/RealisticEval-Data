// Assuming the existence of a ModelAnswerResult class in the same project
class ModelAnswerResult {
    constructor(public result: number) {}
}

function sum(arr: number[]): ModelAnswerResult {
    const total = arr.reduce((acc, curr) => acc + curr, 0);
    return new ModelAnswerResult(total);
}
describe('Sum Function Tests', () => {
    test('should return the sum of a normal array of positive numbers', () => {
        expect(sum([1, 2, 3, 4, 5])).toBe(15);
    });

    test('should return the sum of an array containing negative numbers', () => {
        expect(sum([-1, -2, -3, -4, -5])).toBe(-15);
    });

    test('should return 0 for an empty array', () => {
        expect(sum([])).toBe(0);
    });

    test('should return the sum of an array containing both positive and negative numbers', () => {
        expect(sum([10, -10, 5, -5, 15])).toBe(15);
    });

    test('should return the sum of an array with floating point numbers', () => {
        expect(sum([1.5, 2.5, 3.5])).toBe(7.5);
    });
});
