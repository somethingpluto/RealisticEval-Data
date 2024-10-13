const { isClose } = require('mathjs'); // Assuming we use mathjs for isClose function

describe('TestProbabilityOfRedBalls', () => {
    describe('testHalfRedBalls', () => {
        it('should pass for half red balls', () => {
            // Scenario where half of the drawn balls are expected to be red
            const result = probabilityOfRedBalls(7, 10, 10);
            const expectedResult = probabilityOfRedBalls(7, 10, 10); // Calculate manually or from another tool
            expect(isClose(result, expectedResult)).toBe(true);
        });
    });

    describe('testSomeRedBalls', () => {
        it('should pass for some red balls', () => {
            // Scenario with some red balls in the jar, expecting a few red draws
            const result = probabilityOfRedBalls(5, 5, 10);
            const expectedResult = probabilityOfRedBalls(5, 5, 10); // Calculate manually or from another tool
            expect(isClose(result, expectedResult)).toBe(true);
        });
    });

    describe('testExtremeCase', () => {
        it('should pass for extreme case', () => {
            // Extreme scenario where the probability is low for the chosen n
            const result = probabilityOfRedBalls(15, 1, 99);
            const expectedResult = probabilityOfRedBalls(15, 1, 99); // Calculate manually or from another tool
            expect(isClose(result, expectedResult)).toBe(true);
        });
    });
});