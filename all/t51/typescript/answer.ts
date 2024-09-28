import { NDArray } from 'numeric';
import numeric from 'numeric';

function changeReferenceFrame(pointCloud: NDArray, refFramePoints: NDArray[]): NDArray {
    /**
     * Transforms a point cloud to a new reference frame defined by three points.
     *
     * Parameters:
     *     pointCloud (NDArray): The Nx3 array of points in the original reference frame.
     *     refFramePoints (NDArray[]): A list of three points (NDArray), defining the new reference frame.
     *
     * Returns:
     *     NDArray: Transformed point cloud in the new reference frame.
     */

    // Ensure points and point cloud are in the correct type
    pointCloud = numeric.clone(pointCloud) as NDArray;
    refFramePoints = refFramePoints.map(p => numeric.clone(p)) as NDArray[];

    // Unpack the three points defining the new reference frame
    const [A, B, C] = refFramePoints;

    // Compute the new basis vectors
    const u = numeric.sub(B, A); // Vector from A to B
    const AB = numeric.sub(B, A);
    const AC = numeric.sub(C, A);
    const w = numeric.cross(AB, AC); // Orthogonal vector to the plane defined by A, B, and C
    const v = numeric.cross(w, u); // Vector orthogonal to both u and w

    // Normalize the basis vectors to form an orthonormal basis
    const normalize = (vec: NDArray): NDArray => numeric.div(vec, numeric.norm2(vec));

    const uNorm = normalize(u);
    const vNorm = normalize(v);
    const wNorm = normalize(w);

    // Construct the rotation matrix from the old basis to the new basis
    const rotationMatrix = numeric.transpose([uNorm, vNorm, wNorm]);

    // Calculate the translation vector to shift origin to A
    const translationVector = numeric.dot(numeric.neg(rotationMatrix), A);

    // Apply the rotation and translation to the point cloud
    const transformedPointCloud = numeric.add(
        numeric.dot(numeric.sub(pointCloud, A), rotationMatrix),
        translationVector
    );

    return transformedPointCloud;
}

// Example usage
// Import numeric if not at top level