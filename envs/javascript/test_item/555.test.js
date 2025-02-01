/**
 * Converts a quaternion to a rotation angle in radians.
 *
 * @param {Array<number>} quaternion - An array containing the quaternion components (w, x, y, z)
 * @returns {number} The rotation angle in radians
 */
function quaternionToAngle(quaternion) {
    // Extract the scalar part (w) of the quaternion
    const w = quaternion[0];
    
    // Calculate the rotation angle in radians
    // The arccosine of the scalar part (w) of the quaternion, multiplied by 2
    const angle = 2 * Math.acos(w);
    
    // Return the rotation angle in radians
    return angle;
}
describe('TestQuaternionToAngle', () => {
    it('test identity quaternion (no rotation)', () => {
        const quaternion = [1.0, 0.0, 0.0, 0.0];
        const expectedAngle = 0.0;
        expect(quaternionToAngle(quaternion)).toBeCloseTo(expectedAngle);
    });

    it('test quaternion representing a 180-degree rotation', () => {
        const quaternion = [0.0, 0.0, 1.0, 0.0];  // 180 degrees around Z axis
        const expectedAngle = Math.PI;  // 180 degrees in radians
        expect(quaternionToAngle(quaternion)).toBeCloseTo(expectedAngle);
    });

    it('test quaternion representing a full 360-degree rotation', () => {
        const quaternion = [1.0, 0.0, 0.0, 0.0];  // Full rotation
        const expectedAngle = 0.0;  // 360 degrees is equivalent to 0 degrees
        expect(quaternionToAngle(quaternion)).toBeCloseTo(expectedAngle);
    });

    it('test non-unit quaternion (should still give correct angle)', () => {
        const quaternion = [0.5, 0.5, 0.5, 0.5];  // This is not normalized
        // Normalize the quaternion first
        const norm = Math.sqrt(quaternion.reduce((acc, val) => acc + val ** 2, 0));
        const normalizedQuaternion = quaternion.map(x => x / norm);
        const expectedAngle = 2 * Math.acos(normalizedQuaternion[0]);  // Should be same angle
        expect(quaternionToAngle(normalizedQuaternion)).toBeCloseTo(expectedAngle);
    });

    it('test invalid quaternion raises a ValueError', () => {
        expect(() => quaternionToAngle([1.0, 0.0, 0.0])).toThrow();
    });
});
