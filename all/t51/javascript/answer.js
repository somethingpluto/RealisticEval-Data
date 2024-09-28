// Import math and create an alias for easier access
const math = require('mathjs');

/**
 * Transforms a point cloud to a new reference frame defined by three points.
 *
 * @param {Array} pointCloud - The Nx3 array of points in the original reference frame.
 * @param {Array} refFramePoints - A list of three points (Array), defining the new reference frame.
 * @returns {Array} Transformed point cloud in the new reference frame.
 */
function changeReferenceFrame(pointCloud, refFramePoints) {
    // Convert points to float to avoid type casting errors during operations
    pointCloud = pointCloud.map(point => point.map(coord => parseFloat(coord)));
    refFramePoints = refFramePoints.map(point => point.map(coord => parseFloat(coord)));

    // Unpack the three points defining the new reference frame
    const [A, B, C] = refFramePoints;

    // Compute the new basis vectors
    const u = math.subtract(B, A); // Vector from A to B
    const w = math.cross(u, math.subtract(C, A)); // Orthogonal vector to the plane defined by A, B, and C
    const v = math.cross(w, u); // Vector orthogonal to both u and w

    // Normalize the basis vectors to form an orthonormal basis
    const uNorm = math.divide(u, math.norm(u));
    const vNorm = math.divide(v, math.norm(v));
    const wNorm = math.divide(w, math.norm(w));

    // Construct the rotation matrix from the old basis to the new basis
    const rotationMatrix = math.transpose([uNorm, vNorm, wNorm]);

    // Calculate the translation vector to shift origin to A
    const translationVector = math.multiply(-1, math.multiply(rotationMatrix, A));

    // Apply the rotation and translation to the point cloud
    let transformedPointCloud = pointCloud.map(point => 
        math.add(
            math.multiply(math.subtract(point, A), rotationMatrix),
            translationVector
        )
    );

    return transformedPointCloud;
}

// Example usage (using Node.js)
const pointCloud = [[1,2,3],[4,5,6],[7,8,9]];
const refFramePoints = [[1,0,0],[0,1,0],[0,0,1]];
console.log(changeReferenceFrame(pointCloud, refFramePoints));