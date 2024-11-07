import math from 'mathjs'
function rotatePointCloud(pointCloud, rotationAngle) {
    const rotationMatrix = math.matrix([
        [math.cos(rotationAngle), 0, math.sin(rotationAngle)],
        [0, 1, 0],
        [-math.sin(rotationAngle), 0, math.cos(rotationAngle)]
    ]);

    // Rotate the point cloud by multiplying with the rotation matrix
    const rotatedPointCloud = math.multiply(pointCloud, rotationMatrix);

    return rotatedPointCloud;
}