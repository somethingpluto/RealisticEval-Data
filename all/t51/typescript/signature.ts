/**
 * Transforms a point cloud to a new reference frame defined by three points.
 *
 * @param {number[][]} pointCloud - An array of 3D points where each point is represented 
 * as an array of three numbers [x, y, z]. 
 * Example: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
 *
 * @param {number[][]} refFramePoints - An array of 3D points that define the new reference frame.
 * This is typically an array of at least three non-collinear points. Each point should be 
 * represented as an array of three numbers [x, y, z].
 * Example: [[0, 0, 0], [1, 0, 0], [0, 1, 0]]
 *
 * @returns {number[][]} A new array of 3D points, each transformed to the specified reference frame.
 * The returned array maintains the same structure as the input point cloud.
 * Example: [[1, 2, 3], [4, 5, 6]] will be transformed based on the reference frame points.
 *
 * @throws {Error} Throws an error if the input point cloud or reference frame points are 
 * invalid (e.g., if they do not contain three points, or if any point is not 3-dimensional).
 *
 * @example
 * const pointCloud = [
 *     [1, 2, 3],
 *     [4, 5, 6],
 *     [7, 8, 9]
 * ];
 * 
 * const refFramePoints = [
 *     [0, 0, 0],
 *     [1, 0, 0],
 *     [0, 1, 0]
 * ];
 * 
 */
function transformPointCloudToReferenceFrame(
    pointCloud: number[][],
    refFramePoints: number[][]
): number[][] {}