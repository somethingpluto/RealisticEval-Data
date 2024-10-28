/**
 * Calculates the steering angle based on the given angular velocity, speed, and wheelbase.
 *
 * The function uses the relationship between angular velocity, speed, and the steering angle
 * to determine the appropriate steering angle required for the vehicle to achieve the desired
 * angular velocity. The formula used is:
 *
 *      ω = (v / L) * tan(δ)
 *
 * Rearranging gives us:
 *
 *      δ = atan((ω * L) / v)
 *
 * @param angularVelocity The angular velocity of the vehicle in radians per second.
 * @param speed The forward speed of the vehicle in meters per second.
 * @param wheelbase The distance between the front and rear axles of the vehicle in meters.
 *
 * @return The steering angle in radians.
 *
 * @throws Error if speed is less than or equal to zero,
 *                since the vehicle cannot move at zero or negative speed.
 */
function calculateSteeringAngle(angularVelocity: number, speed: number, wheelbase: number): number {
    if (speed <= 0) {
        throw new Error("Speed must be greater than zero.");
    }

    const steeringAngle = Math.atan((angularVelocity * wheelbase) / speed);
    return steeringAngle;
}
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
