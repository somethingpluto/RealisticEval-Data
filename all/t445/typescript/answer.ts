import * as THREE from 'three';

function createRotMatrix(angleDeg: number, axis: string): THREE.Matrix4 {
    /**
     * Create a pose matrix representing a rotation about a given axis.
     *
     * @param {number} angleDeg - Rotation angle in degrees.
     * @param {string} axis - Axis to rotate about, must be one of 'X', 'Y', or 'Z'.
     * @returns {THREE.Matrix4} - 4x4 pose matrix representing the rotation.
     */

    const angleRad = THREE.MathUtils.degToRad(angleDeg);
    let rotationMatrix: THREE.Matrix4;

    switch (axis.toUpperCase()) {
        case 'X':
            rotationMatrix = new THREE.Matrix4().makeRotationX(angleRad);
            break;
        case 'Y':
            rotationMatrix = new THREE.Matrix4().makeRotationY(angleRad);
            break;
        case 'Z':
            rotationMatrix = new THREE.Matrix4().makeRotationZ(angleRad);
            break;
        default:
            throw new Error("Invalid axis. Must be 'X', 'Y', or 'Z'.");
    }

    return rotationMatrix;
}
