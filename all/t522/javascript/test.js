describe('rotatePointCloud', () => {
  
  test('no rotation (rotation angle is 0)', () => {
    // Test when the rotation angle is 0 (should return the same point cloud)
    const pointCloud = [[1.0, 2.0, 3.0]];
    const rotationAngle = 0;
    const expectedOutput = pointCloud;

    const result = rotatePointCloud(pointCloud, rotationAngle);
    
    // Check if the result matches the expected output
    expect(result).toEqual(expectedOutput);
  });

  test('180-degree rotation (π radians)', () => {
    // Test rotation of 180 degrees (π radians) around Y axis
    const pointCloud = [
      [1.0, 0.0, 0.0], 
      [0.0, 1.0, 0.0]
    ];
    const rotationAngle = Math.PI;  // 180 degrees
    const expectedOutput = [
      [-1.0, 0.0, 0.0], 
      [0.0, 1.0, 0.0]
    ];

    const result = rotatePointCloud(pointCloud, rotationAngle);
    
    // Check if the result matches the expected output
    expect(result).toEqual(expectedOutput);
  });

  test('full rotation (360 degrees or 2π radians)', () => {
    // Test rotation of 360 degrees (2π radians) around Y axis (should return the same point cloud)
    const pointCloud = [[1.0, 2.0, 3.0]];
    const rotationAngle = 2 * Math.PI;  // 360 degrees
    const expectedOutput = pointCloud; // Should return the same point cloud

    const result = rotatePointCloud(pointCloud, rotationAngle);
    
    // Check if the result matches the expected output
    expect(result).toEqual(expectedOutput);
  });

});
