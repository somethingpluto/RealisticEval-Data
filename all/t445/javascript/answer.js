function createRotMatrix(angleDeg, axis) {
    const angleRad = angleDeg * (Math.PI / 180);

    // Define the rotation matrix based on the specified axis
    let rotationMatrix;
    if (axis.toLowerCase() === 'x') {
        rotationMatrix = [
            [1, 0, 0, 0],
            [0, Math.cos(angleRad), -Math.sin(angleRad), 0],
            [0, Math.sin(angleRad), Math.cos(angleRad), 0],
            [0, 0, 0, 1]
        ];
    } else if (axis.toLowerCase() === 'y') {
        rotationMatrix = [
            [Math.cos(angleRad), 0, Math.sin(angleRad), 0],
            [0, 1, 0, 0],
            [-Math.sin(angleRad), 0, Math.cos(angleRad), 0],
            [0, 0, 0, 1]
        ];
    } else if (axis.toLowerCase() === 'z') {
        rotationMatrix = [
            [Math.cos(angleRad), -Math.sin(angleRad), 0, 0],
            [Math.sin(angleRad), Math.cos(angleRad), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ];
    } else {
        throw new Error("Invalid axis. Must be one of 'X', 'Y', or 'Z'.");
    }

    return rotationMatrix;
}