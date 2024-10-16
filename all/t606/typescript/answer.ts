function calculateSteeringAngle(angularVelocity: number, speed: number, wheelbase: number): number {
    // Check for valid speed
    if (speed <= 0) {
        throw new Error("Speed must be greater than zero.");
    }

    // Calculate steering angle in radians
    const steeringAngle: number = Math.atan((angularVelocity * wheelbase) / speed);

    return steeringAngle; // Returns the steering angle in radians
}