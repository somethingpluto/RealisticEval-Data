describe('probabilityOfRedBalls', () => {
    it('should calculate the probability correctly', () => {
        expect(probabilityOfRedBalls(3, 6, 9)).toBeCloseTo(0.4861111111111111);
        expect(probabilityOfRedBalls(5, 10, 5)).toBeCloseTo(0.1736111111111111);
        expect(probabilityOfRedBalls(0, 0, 15)).toBeCloseTo(0.0003586175000000001);
    });

    it('should handle invalid inputs', () => {
        expect(() => probabilityOfRedBalls(4, 6, 9)).toThrowError("Invalid input");
        expect(() => probabilityOfRedBalls(6, 10, 5)).toThrowError("Invalid input");
        expect(() => probabilityOfRedBalls(3, 3, 12)).toThrowError("Invalid input");
    });
});