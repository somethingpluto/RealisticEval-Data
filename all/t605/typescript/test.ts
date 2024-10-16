describe("BMI calculations", () => {
    // Test case for valid inputs with expected BMI value
    describe("Valid BMI calculations", () => {
        test("Normal weight", () => {
            expect(calculateBMI(70, 1.75)).toBeCloseTo(22.86, 2); // 70 kg, 1.75 m
        });

        test("Underweight", () => {
            expect(calculateBMI(50, 1.75)).toBeCloseTo(16.33, 2); // 50 kg, 1.75 m
        });

        test("Overweight", () => {
            expect(calculateBMI(80, 1.75)).toBeCloseTo(26.12, 2); // 80 kg, 1.75 m
        });

        test("Obesity", () => {
            expect(calculateBMI(100, 1.75)).toBeCloseTo(32.65, 2); // 100 kg, 1.75 m
        });
    });

    // Test case for invalid inputs
    describe("Invalid BMI calculations", () => {
        test("Negative weight", () => {
            expect(() => calculateBMI(-70, 1.75)).toThrow(Error); // Negative weight
        });

        test("Zero height", () => {
            expect(() => calculateBMI(70, 0)).toThrow(Error); // Zero height
        });

        test("Negative height", () => {
            expect(() => calculateBMI(70, -1.75)).toThrow(Error); // Negative height
        });
    });
});