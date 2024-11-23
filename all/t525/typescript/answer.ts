function flipPointCloud(pointCloud: number[][], axis: number): number[][] {
    if (axis !== 0 && axis !== 1 && axis !== 2) {
        throw new Error("Axis must be 0 (x-axis), 1 (y-axis), or 2 (z-axis).");
    }

    // Create a scaling factor array with -1 for the specified axis and 1 for others
    const flipFactors: number[] = [1, 1, 1];
    flipFactors[axis] = -1;

    // Flip the point cloud by multiplying with the scaling factor array
    const flippedPointCloud: number[][] = pointCloud.map(row => {
        return row.map((value, index) => value * flipFactors[index]);
    });

    return flippedPointCloud;
}
