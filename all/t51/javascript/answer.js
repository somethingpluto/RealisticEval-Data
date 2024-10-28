/**
 * Transforms a point cloud to a new reference frame defined by three points.
 *
 * @param {Float64Array} pointCloud - The Nx3 array of points in the original reference frame.
 * @param {Array<Float64Array>} refFramePoints - A list of three Float64Arrays, defining the new reference frame.
 * @returns {Float64Array} Transformed point cloud in the new reference frame.
 */
function transformPointCloudToReferenceFrame(pointCloud, refFramePoints) {
    // Convert points to Float64Arrays
    const A = refFramePoints[0];
    const B = refFramePoints[1];
    const C = refFramePoints[2];

    // Compute the new basis vectors
    const u = new Float64Array(3);
    const w = new Float64Array(3);
    const v = new Float64Array(3);

    // Vector from A to B
    u[0] = B[0] - A[0];
    u[1] = B[1] - A[1];
    u[2] = B[2] - A[2];

    // Orthogonal vector to the plane defined by A, B, and C
    w[0] = u[1] * (C[2] - A[2]) - u[2] * (C[1] - A[1]);
    w[1] = u[2] * (C[0] - A[0]) - u[0] * (C[2] - A[2]);
    w[2] = u[0] * (C[1] - A[1]) - u[1] * (C[0] - A[0]);

    // Normalize the basis vectors
    const normU = Math.sqrt(u[0] ** 2 + u[1] ** 2 + u[2] ** 2);
    const normW = Math.sqrt(w[0] ** 2 + w[1] ** 2 + w[2] ** 2);
    const normV = Math.sqrt(v[0] ** 2 + v[1] ** 2 + v[2] ** 2);

    for (let i = 0; i < 3; i++) {
        u[i] /= normU;
        w[i] /= normW;
    }

    // Calculate v using the cross product
    v[0] = w[1] * u[2] - w[2] * u[1];
    v[1] = w[2] * u[0] - w[0] * u[2];
    v[2] = w[0] * u[1] - w[1] * u[0];

    // Calculate translation vector to shift origin to A
    const rotationMatrix = [u, v, w];
    const translationVector = new Float64Array(3);
    for (let i = 0; i < 3; i++) {
        translationVector[i] = -(rotationMatrix[0][i] * A[0] + rotationMatrix[1][i] * A[1] + rotationMatrix[2][i] * A[2]);
    }

    // Apply the rotation and translation to the point cloud
    const transformedPointCloud = new Float64Array(pointCloud.length);
    for (let i = 0; i < pointCloud.length / 3; i++) {
        const index = i * 3;
        const point = new Float64Array(3);

        for (let j = 0; j < 3; j++) {
            point[j] = pointCloud[index + j] - A[j]; // Translate to origin A
        }

        // Apply rotation
        for (let j = 0; j < 3; j++) {
            transformedPointCloud[index + j] = rotationMatrix[j][0] * point[0] +
                                                rotationMatrix[j][1] * point[1] +
                                                rotationMatrix[j][2] * point[2] + 
                                                translationVector[j]; // Apply translation
        }
    }

    return transformedPointCloud;
}
