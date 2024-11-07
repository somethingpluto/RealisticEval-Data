function quaternionToAngle(quaternion: [number, number, number, number]): number {
    // Ensure the quaternion is a valid 4-element array
    if (quaternion.length !== 4) {
        throw new Error("Quaternion must have 4 components (w, x, y, z)");
    }

    const [w, x, y, z] = quaternion;

    // Calculate the angle in radians
    const angle = 2 * Math.acos(w);

    return angle;
}
