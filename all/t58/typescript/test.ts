describe('probability_of_red_balls', () => {
    test('should calculate the probability correctly', () => {
        expect(probability_of_red_balls(3, 5, 10)).toBeCloseTo(0.2667);
        expect(probability_of_red_balls(2, 4, 6)).toBeCloseTo(0.4286);
        expect(probability_of_red_balls(0, 3, 7)).toBeCloseTo(0.3125);
        expect(probability_of_red_balls(5, 5, 5)).toBeCloseTo(0.2461);
        expect(probability_of_red_balls(1, 0, 0)).toBe(0);
        expect(probability_of_red_balls(3, 3, 0)).toBe(0);
        expect(probability_of_red_balls(3, 0, 3)).toBe(0);
        expect(probability_of_red_balls(3, 3, 3)).toBeCloseTo(0.2963);
    });

    test('should handle edge cases', () => {
        expect(probability_of_red_balls(-1, 5, 10)).toBe(0);
        expect(probability_of_red_balls(6, 5, 10)).toBe(0);
        expect(probability_of_red_balls(3, 2, 1)).toBe(0);
    });
});