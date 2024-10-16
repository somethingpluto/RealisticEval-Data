describe("Calculate Steering Angle Tests", () => {
    const wheelbase = 2.5; // Setting wheelbase constant for all tests

    test("Normal case", () => {
        const angularVelocity = 1.0; // radians/second
        const speed = 10.0;          // meters/second
        const expectedAngle = Math.atan((angularVelocity * wheelbase) / speed);
        expect(calculateSteeringAngle(angularVelocity, speed, wheelbase)).toBeCloseTo(expectedAngle);
    });

    test("Zero speed", () => {
        const angularVelocity = 1.0; // radians/second
        const speed = 0.0;           // meters/second
        expect(() => calculateSteeringAngle(angularVelocity, speed, wheelbase)).toThrow(Error);
    });

    test("Negative speed", () => {
        const angularVelocity = 1.0; // radians/second
        const speed = -5.0;          // meters/second
        expect(() => calculateSteeringAngle(angularVelocity, speed, wheelbase)).toThrow(Error);
    });

    test("Zero angular velocity", () => {
        const angularVelocity = 0.0; // radians/second
        const speed = 10.0;          // meters/second
        const expectedAngle = 0.0;   // Steering angle should be zero
        expect(calculateSteeringAngle(angularVelocity, speed, wheelbase)).toBeCloseTo(expectedAngle);
    });

    test("Large values", () => {
        const angularVelocity = 100.0; // radians/second
        const speed = 1000.0;          // meters/second
        const expectedAngle = Math.atan((angularVelocity * wheelbase) / speed);
        expect(calculateSteeringAngle(angularVelocity, speed, wheelbase)).toBeCloseTo(expectedAngle);
    });

    test("High angular velocity", () => {
        const angularVelocity = 10.0; // radians/second
        const speed = 1.0;             // meters/second
        const expectedAngle = Math.atan((angularVelocity * wheelbase) / speed);
        expect(calculateSteeringAngle(angularVelocity, speed, wheelbase)).toBeCloseTo(expectedAngle);
    });
});