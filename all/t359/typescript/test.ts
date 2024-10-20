import Math from 'mathjs'; // Importing mathjs for mathematical constants

describe("TrapezoidalRule Test Cases", () => {
    // Test Case 1: Integration of a constant function (f(x) = 1) over [0, 1]
    test("Integration of constant function (f(x) = 1) over [0, 1]", () => {
        expect(trapezoidalRule((x) => 1.0, 0.0, 1.0, 100)).toBeCloseTo(1.0, 6);
    });

    // Test Case 2: Integration of a linear function (f(x) = x) over [0, 1]
    test("Integration of linear function (f(x) = x) over [0, 1]", () => {
        expect(trapezoidalRule((x) => x, 0.0, 1.0, 100)).toBeCloseTo(0.5, 6);
    });

    // Test Case 3: Integration of a quadratic function (f(x) = x^2) over [0, 1]
    test("Integration of quadratic function (f(x) = x^2) over [0, 1]", () => {
        expect(trapezoidalRule((x) => x * x, 0.0, 1.0, 1000)).toBeCloseTo(1.0 / 3.0, 6);
    });

    // Test Case 4: Integration of the sine function (f(x) = sin(x)) over [0, π]
    test("Integration of sine function (f(x) = sin(x)) over [0, π]", () => {
        expect(trapezoidalRule((x) => Math.sin(x), 0.0, Math.PI, 1000)).toBeCloseTo(2.0, 6);
    });

    // Test Case 5: Integration of an exponential function (f(x) = exp(x)) over [0, 1]
    test("Integration of exponential function (f(x) = exp(x)) over [0, 1]", () => {
        expect(trapezoidalRule((x) => Math.exp(x), 0.0, 1.0, 1000)).toBeCloseTo(Math.exp(1.0) - 1.0, 6);
    });
});