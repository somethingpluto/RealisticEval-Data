// Import necessary packages
const _ = require('lodash'); // For deep equality check
const math = require('mathjs'); // For matrix operations

/**
 * Translate the point cloud by a given vector.
 *
 * @param {Array<Array<number>>} pointCloud - An N x 3 array representing the 3D point cloud.
 * @param {Array<number>} translationVector - A 1 x 3 array representing the translation vector.
 * @returns {Array<Array<number>>} - An N x 3 array of the translated point cloud.
 */
function translatePointCloud(pointCloud, translationVector) {
    // Ensure the translationVector is an array for broadcasting
    translationVector = Array.isArray(translationVector) ? translationVector : [translationVector];

    // Check if translationVector is of correct shape
    if (translationVector.length !== 3) {
        throw new Error("translationVector must be a 1D array of length 3");
    }

    // Translate the point cloud by adding the translation vector to each point
    const translatedPointCloud = pointCloud.map(point => {
        return [
            point[0] + translationVector[0],
            point[1] + translationVector[1],
            point[2] + translationVector[2]
        ];
    });

    return translatedPointCloud;
}