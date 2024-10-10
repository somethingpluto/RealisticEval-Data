describe('probabilityRedBalls', () => {
    it('should calculate the probability correctly when all drawn balls are red', () => {
        expect(probabilityRedBalls(3, 5, 2)).toBeCloseTo(0.4667);
    });

    it('should calculate the probability correctly when no balls are drawn', () => {
        expect(probabilityRedBalls(0, 5, 2)).toBeCloseTo(1);
    });

    it('should return 0 when more balls are drawn than available red balls', () => {
        expect(probabilityRedBalls(6, 5, 2)).toBeCloseTo(0);
    });

    it('should return 0 when more balls are drawn than available total balls', () => {
        expect(probabilityRedBalls(8, 5, 2)).toBeCloseTo(0);
    });
});