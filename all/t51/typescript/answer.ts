import { create, all } from 'mathjs';
const math = create(all);

function transformPointCloudToReferenceFrame(
    pointCloud: number[][],
    refFramePoints: number[][]
): number[][] {
    // Ensure the point cloud is in the correct format (Nx3)
    if (pointCloud.length === 0 || pointCloud[0].length !== 3) {
        throw new Error('pointCloud must be a non-empty Nx3 array.');
    }

    if (refFramePoints.length !== 3 || refFramePoints.some(p => p.length !== 3)) {
        throw new Error('refFramePoints must be an array of three 3D points.');
    }

    // Convert points to float to avoid type casting errors
    const A = math.matrix(refFramePoints[0]);
    const B = math.matrix(refFramePoints[1]);
    const C = math.matrix(refFramePoints[2]);

    // Compute the new basis vectors
    const u = math.subtract(B, A); // Vector from A to B
    const w = math.cross(u, math.subtract(C, A)); // Orthogonal vector to the plane defined by A, B, and C
    const v = math.cross(w, u); // Vector orthogonal to both u and w

    // Normalize the basis vectors to form an orthonormal basis
    const normU = math.norm(u);
    const normW = math.norm(w);
    const normV = math.norm(v);
    const normalizedU = math.multiply(u, 1 / normU);
    const normalizedW = math.multiply(w, 1 / normW);
    const normalizedV = math.multiply(v, 1 / normV);

    // Construct the rotation matrix from the old basis to the new basis
    const rotationMatrix = math.concat(normalizedU, normalizedV, normalizedW, 1);

    // Calculate the translation vector to shift origin to A
    const translationVector = math.multiply(rotationMatrix, math.unaryMinus(A));

    // Transform point cloud using rotation and translation
    const transformedPointCloud = pointCloud.map(point => {
        const pointMatrix = math.matrix(point);
        const rotatedPoint = math.add(math.multiply(math.subtract(pointMatrix, A), rotationMatrix), translationVector);
        return rotatedPoint.valueOf() as number[];
    });

    return transformedPointCloud;
}
